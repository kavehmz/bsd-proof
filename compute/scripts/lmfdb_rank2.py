#!/usr/bin/env python3
"""
lmfdb_rank2.py -- query the LMFDB API for elliptic curves over Q of rank >= 2.

Run with the wrapper (Python 3.11 from .tools/env) or /usr/bin/python3 (stdlib only):

    compute/scripts/python compute/scripts/lmfdb_rank2.py --all

Sub-tasks (each writes files into compute/data/, see compute/README.md):

  --fields     fetch one record of ec_curvedata and ec_mwbsd to learn the exact field
               names                                  -> lmfdb_fields.json
  --sha        list all curves with rank >= 2, sha != 1, conductor < 500000
                                                      -> lmfdb_rank_ge2_sha_ne1_N_lt_500000.{json,csv}
               and pick the 10 rank-2 curves of smallest conductor with sha > 1
                                                      -> lmfdb_rank2_sha_picks.{json,gp}
  --rank34     list all rank-3 and rank-4 curves with conductor < 500000
                                                      -> lmfdb_rank3_N_lt_500000.{json,csv}, lmfdb_rank4_...
  --counts     count rank 2, 3, 4 curves by conductor range (by exhaustive enumeration of
               `id`s in conductor slices; the API has no count endpoint and caps the offset
               at 10000, so slices are split adaptively)  -> lmfdb_rank_counts_by_conductor.{json,csv}
  --reference  fetch LMFDB's BSD data (ec_mwbsd: real_period, regulator, tamagawa_product,
               special_value, sha_an) for the curves of the BSD table, for cross-checking
                                                      -> lmfdb_bsd_reference.json
  --compare F  compare the analytic Sha in our bsd_table output F (TSV written by
               compute/scripts/bsd_table.gp) with LMFDB's `sha` and `sha_an`

API notes (learned from https://www.lmfdb.org/api/ and lmfdb/api/api.py):
  * typed equality:  rank=i2  (i=int, s=string, f=float, li=list of ints, py=Python literal)
  * a `py` value is passed to the database layer verbatim, so range queries work as
    conductor=py{"$lt":500000}  or  conductor=py{"$gte":100000,"$lt":200000}, and sha=py{"$ne":1}
  * pagination: 100 records per page, `_offset=k`, offset must be <= 10000
  * `_fields=a,b,c` projection, `_sort=conductor`
  * requests without a browser-like flow are sometimes served a reCAPTCHA page for the HTML
    format; the JSON API (`_format=json`) has always answered for us. We sleep between requests.
"""
import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://www.lmfdb.org/api/"
UA = "bsd-conjecture-compute/0.1 (PARI/GP BSD laboratory; python urllib; polite, sequential)"
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
NMAX = 500000  # conductor bound (exclusive): conductor < 500000
SLEEP = 0.15   # seconds between requests
NREQ = 0       # request counter (reported in outputs)

BSD_TABLE_CURVES = ["11a1", "37a1", "389a1", "433a1", "446d1", "563a1", "571b1", "643a1", "655a1",
                    "664a1", "681c1", "707a1", "709a1", "718b1", "794a1", "817a1", "916c1", "944e1",
                    "997b1", "1001c1", "1058d1", "5077a1"]

CONDUCTOR_RANGES = [(1, 10**3), (10**3, 10**4), (10**4, 10**5), (10**5, 2 * 10**5),
                    (2 * 10**5, 3 * 10**5), (3 * 10**5, 4 * 10**5), (4 * 10**5, 5 * 10**5)]


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def api_url(table, params):
    # keep {}$": , unescaped so that the py{...} dict values stay readable in the logs (urllib
    # quotes them anyway when needed; LMFDB accepts both forms)
    return BASE + table + "/?" + urllib.parse.urlencode(params, safe='{}$":,')


def api_get(table, params, retries=6):
    """One API request; returns the parsed JSON document."""
    global NREQ
    url = api_url(table, params)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=180) as r:
                body = r.read()
            NREQ += 1
            time.sleep(SLEEP)
            if body.lstrip().startswith(b"<") and b"recaptcha" in body[:2000].lower():
                raise ValueError("LMFDB served a reCAPTCHA challenge page (bot protection / rate limit)")
            doc = json.loads(body)
            if "data" not in doc:
                raise ValueError("no 'data' in response")
            return doc
        except (urllib.error.URLError, ValueError, json.JSONDecodeError) as e:
            wait = 30 * (attempt + 1) if "reCAPTCHA" in str(e) else 5 * (attempt + 1)
            log(f"  request failed ({e}); retrying in {wait}s: {url}")
            time.sleep(wait)
    raise RuntimeError("LMFDB API request failed repeatedly: " + url)


def api_all(table, params, hard_cap=10000):
    """Paginate a query (100 records per page). Returns (records, hit_cap)."""
    out = []
    offset = 0
    while True:
        p = dict(params)
        p["_format"] = "json"
        p["_offset"] = offset
        doc = api_get(table, p)
        data = doc["data"]
        out.extend(data)
        if len(data) < 100:
            return out, False
        offset += len(data)
        if offset >= hard_cap:
            # LMFDB refuses offsets > 10000; caller must split the query
            return out, True


def cond_range(a, b):
    return 'py{"$gte":%d,"$lt":%d}' % (a, b)


def count_range(rank, a, b, depth=0):
    """Number of curves with given rank and a <= conductor < b, by enumeration of ids."""
    recs, capped = api_all("ec_curvedata", {"rank": "i%d" % rank, "conductor": cond_range(a, b),
                                            "_fields": "id"})
    if not capped:
        return len(recs)
    if b - a <= 1:
        raise RuntimeError("more than 10000 curves at a single conductor?!")
    m = (a + b) // 2
    log(f"  rank {rank}: slice [{a},{b}) exceeds 10000 results, splitting at {m}")
    return count_range(rank, a, m, depth + 1) + count_range(rank, m, b, depth + 1)


def write_json(name, obj):
    path = os.path.join(DATA, name)
    with open(path, "w") as f:
        json.dump(obj, f, indent=1, sort_keys=True)
    log("wrote", path)


def write_csv(name, rows, fields):
    path = os.path.join(DATA, name)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            rr = {k: (json.dumps(v) if isinstance(v, (list, dict)) else v) for k, v in r.items()}
            w.writerow(rr)
    log("wrote", path)


def real_literal(v):
    """LMFDB encodes reals as {'__RealLiteral__':0,'data':'1.23...','prec':97}; return the string."""
    if isinstance(v, dict) and "data" in v:
        return v["data"]
    return v


# ----------------------------------------------------------------------------------------------
def task_fields():
    out = {}
    for table in ["ec_curvedata", "ec_mwbsd", "ec_localdata"]:
        doc = api_get(table, {"_format": "json", "_offset": 0})
        rec = doc["data"][0]
        out[table] = {"fields": sorted(rec.keys()), "example": rec}
    out["_query_syntax"] = {
        "typed equality": "rank=i2, torsion=i5, Clabel=s389a1, lmfdb_label=s389.a1",
        "range (Python literal passed to the DB layer)": 'conductor=py{"$lt":500000}, sha=py{"$ne":1}, rank=py{"$gte":2}',
        "pagination": "_offset=k (100 per page, k<=10000), _fields=a,b,c, _sort=conductor, _format=json",
    }
    write_json("lmfdb_fields.json", out)


CURVE_FIELDS = ["Clabel", "lmfdb_label", "conductor", "rank", "analytic_rank", "sha", "sha_primes",
                "torsion", "torsion_structure", "ainvs", "optimality", "manin_constant", "cm",
                "semistable", "bad_primes", "regulator", "signD", "num_bad_primes"]


def task_sha():
    params = {"rank": 'py{"$gte":2}', "sha": 'py{"$ne":1}', "conductor": 'py{"$lt":%d}' % NMAX,
              "_fields": ",".join(CURVE_FIELDS), "_sort": "conductor,lmfdb_label"}
    recs, capped = api_all("ec_curvedata", params)
    assert not capped
    for r in recs:
        r["regulator"] = real_literal(r.get("regulator"))
    meta = {"query": api_url("ec_curvedata", dict(params, _format="json")),
            "count": len(recs), "date": time.strftime("%Y-%m-%d"),
            "note": "rank>=2, sha!=1 (LMFDB `sha` = analytic order of Sha, rounded), conductor<500000"}
    write_json("lmfdb_rank_ge2_sha_ne1_N_lt_500000.json", {"meta": meta, "data": recs})
    write_csv("lmfdb_rank_ge2_sha_ne1_N_lt_500000.csv", recs, CURVE_FIELDS)

    # the 10 rank-2 curves with sha > 1 of smallest conductor
    picks = [r for r in recs if r["rank"] == 2 and r["sha"] and r["sha"] > 1]
    picks.sort(key=lambda r: (r["conductor"], r["lmfdb_label"]))
    picks = picks[:10]
    for r in picks:
        try:
            doc = api_get("ec_mwbsd", {"_format": "json", "lmfdb_label": "s" + r["lmfdb_label"]}, retries=2)
            mw = doc["data"][0] if doc["data"] else {}
            r["mwbsd"] = {k: real_literal(v) for k, v in mw.items() if k != "id"}
        except RuntimeError as e:
            log("  (ec_mwbsd unavailable for %s: %s)" % (r["lmfdb_label"], e))
            r["mwbsd"] = {}
    write_json("lmfdb_rank2_sha_picks.json", {"meta": {"note": "10 rank-2 curves with sha>1 of smallest conductor, "
                                                              "from lmfdb_rank_ge2_sha_ne1_N_lt_500000.json"},
                                              "data": picks})
    # GP-readable version: vector of [Clabel, lmfdb_label, ainvs, sha, conductor]
    path = os.path.join(DATA, "lmfdb_rank2_sha_picks.gp")
    with open(path, "w") as f:
        f.write("\\\\ generated by compute/scripts/lmfdb_rank2.py --sha ; [Clabel, lmfdb_label, ainvs, sha, conductor]\n")
        f.write("LMFDB_PICKS = [\n")
        for i, r in enumerate(picks):
            sep = "," if i < len(picks) - 1 else ""
            f.write('  ["%s", "%s", %s, %d, %d]%s\n' % (r.get("Clabel") or "", r["lmfdb_label"],
                                                       json.dumps(r["ainvs"]), r["sha"], r["conductor"], sep))
        f.write("];\n")
    log("wrote", path)


def task_rank34():
    for rank in [3, 4]:
        params = {"rank": "i%d" % rank, "conductor": 'py{"$lt":%d}' % NMAX,
                  "_fields": ",".join(CURVE_FIELDS), "_sort": "conductor,lmfdb_label"}
        recs, capped = api_all("ec_curvedata", params)
        if capped:  # more than 10000: enumerate in slices instead
            recs = []
            for (a, b) in CONDUCTOR_RANGES:
                rr, c2 = api_all("ec_curvedata", dict(params, conductor=cond_range(a, b)))
                assert not c2, "rank-%d slice [%d,%d) too large" % (rank, a, b)
                recs.extend(rr)
        for r in recs:
            r["regulator"] = real_literal(r.get("regulator"))
        meta = {"query": api_url("ec_curvedata", dict(params, _format="json")), "count": len(recs),
                "date": time.strftime("%Y-%m-%d")}
        write_json("lmfdb_rank%d_N_lt_500000.json" % rank, {"meta": meta, "data": recs})
        write_csv("lmfdb_rank%d_N_lt_500000.csv" % rank, recs, CURVE_FIELDS)
        nsha = sum(1 for r in recs if r["sha"] and r["sha"] > 1)
        log(f"rank {rank}: {len(recs)} curves with conductor < {NMAX}, {nsha} with sha > 1")


def task_counts():
    global NREQ
    rows = []
    for (a, b) in CONDUCTOR_RANGES:
        row = {"conductor_min": a, "conductor_max_exclusive": b}
        for rank in [2, 3, 4]:
            n0 = NREQ
            t0 = time.time()
            row["rank%d" % rank] = count_range(rank, a, b)
            row["requests_rank%d" % rank] = NREQ - n0
            log(f"[{a},{b}) rank {rank}: {row['rank%d' % rank]}  ({NREQ - n0} requests, {time.time()-t0:.0f}s)")
        rows.append(row)
        # write after every range so that partial results survive an interruption
        tot = {"rank%d" % r: sum(x["rank%d" % r] for x in rows) for r in [2, 3, 4]}
        write_json("lmfdb_rank_counts_by_conductor.json",
                   {"meta": {"method": "exhaustive enumeration of ec_curvedata ids via the API, "
                                       "query rank=i<r>&conductor=py{\"$gte\":a,\"$lt\":b}&_fields=id, "
                                       "100 per page, slices split when >10000 results",
                             "date": time.strftime("%Y-%m-%d"), "total_requests": NREQ,
                             "totals_conductor_lt_500000": tot},
                    "data": rows})
        write_csv("lmfdb_rank_counts_by_conductor.csv", rows,
                  ["conductor_min", "conductor_max_exclusive", "rank2", "rank3", "rank4",
                   "requests_rank2", "requests_rank3", "requests_rank4"])


def task_reference(curves):
    out = {}
    for lab in curves:
        doc = api_get("ec_curvedata", {"_format": "json", "Clabel": "s" + lab,
                                       "_fields": ",".join(CURVE_FIELDS)})
        if not doc["data"]:
            log("no ec_curvedata record for", lab)
            continue
        cd = doc["data"][0]
        cd["regulator"] = real_literal(cd.get("regulator"))
        doc2 = api_get("ec_mwbsd", {"_format": "json", "lmfdb_label": "s" + cd["lmfdb_label"]})
        mw = doc2["data"][0] if doc2["data"] else {}
        mw = {k: real_literal(v) for k, v in mw.items() if k != "id"}
        if "heights" in mw:
            mw["heights"] = [real_literal(h) for h in mw["heights"]]
        out[lab] = {"curvedata": cd, "mwbsd": mw}
        log(lab, "->", cd["lmfdb_label"], "rank", cd["rank"], "sha", cd["sha"], "sha_an", mw.get("sha_an"))
    write_json("lmfdb_bsd_reference.json", {"meta": {"date": time.strftime("%Y-%m-%d"),
                                                     "note": "LMFDB ec_curvedata + ec_mwbsd records for the BSD-table curves"},
                                            "data": out})


# ----------------------------------------------------------------------------------------------
# Cremona's ecdata (the source of LMFDB's ec_curvedata for N <= 500000):
#   https://github.com/JohnCremona/ecdata  (files allcurves.*, allbigsha.*, allbsd.*; format in docs/file-format.txt)
# We use it for exact counts by rank and conductor (the LMFDB API has no count endpoint and
# rate-limits/CAPTCHAs bulk enumeration) and as a second, independent source for BSD reference data.
ECDATA_RAW = "https://raw.githubusercontent.com/JohnCremona/ecdata/master/"
ECDATA_CACHE = os.path.normpath(os.path.join(HERE, "..", "..", ".tools", "ecdata"))
ECDATA_CHUNKS = ["%05d-%05d" % (a, a + 9999) if a < 100000 else "%d-%d" % (a, a + 9999)
                 for a in range(0, NMAX, 10000)]


def ecdata_file(kind, chunk):
    """Download (once) and return the local path of e.g. allcurves/allcurves.00000-09999."""
    os.makedirs(os.path.join(ECDATA_CACHE, kind), exist_ok=True)
    name = "%s.%s" % (kind, chunk)
    path = os.path.join(ECDATA_CACHE, kind, name)
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        url = ECDATA_RAW + kind + "/" + name
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=300) as r, open(path + ".part", "wb") as f:
                    f.write(r.read())
                os.replace(path + ".part", path)
                break
            except urllib.error.URLError as e:
                log(f"  download failed ({e}); retrying: {url}")
                time.sleep(5 * (attempt + 1))
        else:
            raise RuntimeError("could not download " + url)
        log("downloaded", url)
    return path


def task_ecdata():
    """Counts of rank 2,3,4 curves by conductor range, rank-3/4 lists, and the rank>=2, Sha>1 list,
    all from Cremona's ecdata; cross-checked against the API outputs when those exist."""
    counts = {(a, b): {2: 0, 3: 0, 4: 0, "all": 0} for (a, b) in CONDUCTOR_RANGES}
    rank_hist = {}
    rank34 = {3: [], 4: []}
    ncurves = 0
    for chunk in ECDATA_CHUNKS:
        path = ecdata_file("allcurves", chunk)
        with open(path) as f:
            for line in f:
                parts = line.split()
                if len(parts) < 6:
                    continue
                N = int(parts[0])
                if N >= NMAX:
                    continue
                r = int(parts[4])
                ncurves += 1
                rank_hist[r] = rank_hist.get(r, 0) + 1
                for (a, b) in CONDUCTOR_RANGES:
                    if a <= N < b:
                        counts[(a, b)]["all"] += 1
                        if r in (2, 3, 4):
                            counts[(a, b)][r] += 1
                        break
                if r >= 3:
                    rank34[min(r, 4)].append({"Clabel": parts[0] + parts[1] + parts[2], "conductor": N,
                                              "ainvs": parts[3], "rank": r, "torsion": int(parts[5])})
    rows = []
    for (a, b) in CONDUCTOR_RANGES:
        c = counts[(a, b)]
        rows.append({"conductor_min": a, "conductor_max_exclusive": b, "all_curves": c["all"],
                     "rank2": c[2], "rank3": c[3], "rank4": c[4]})
    tot = {"all_curves": ncurves, "by_rank": {str(k): v for k, v in sorted(rank_hist.items())}}
    write_json("ecdata_rank_counts_by_conductor.json",
               {"meta": {"source": ECDATA_RAW + "allcurves/allcurves.<range>", "date": time.strftime("%Y-%m-%d"),
                         "conductor_bound_exclusive": NMAX, "totals": tot}, "data": rows})
    write_csv("ecdata_rank_counts_by_conductor.csv", rows,
              ["conductor_min", "conductor_max_exclusive", "all_curves", "rank2", "rank3", "rank4"])
    log("ecdata totals (N<%d): %s" % (NMAX, tot))

    # rank >= 2 with Sha > 1, from allbigsha
    big = []
    for chunk in ECDATA_CHUNKS:
        path = ecdata_file("allbigsha", chunk)
        with open(path) as f:
            for line in f:
                parts = line.split()
                if len(parts) < 7:
                    continue
                N = int(parts[0])
                if N >= NMAX:
                    continue
                r = int(parts[4])
                if r >= 2:
                    big.append({"Clabel": parts[0] + parts[1] + parts[2], "conductor": N, "ainvs": parts[3],
                                "rank": r, "torsion": int(parts[5]), "sha": parts[6]})
    big.sort(key=lambda x: (x["conductor"], x["Clabel"]))
    write_json("ecdata_rank_ge2_sha_gt1_N_lt_500000.json",
               {"meta": {"source": ECDATA_RAW + "allbigsha/allbigsha.<range>", "count": len(big),
                         "date": time.strftime("%Y-%m-%d")}, "data": big})
    write_csv("ecdata_rank_ge2_sha_gt1_N_lt_500000.csv", big, ["Clabel", "conductor", "ainvs", "rank", "torsion", "sha"])
    log("ecdata: %d curves with rank>=2 and Sha>1, N<%d" % (len(big), NMAX))
    for rank in (3, 4):
        write_csv("ecdata_rank%d_N_lt_500000.csv" % rank, rank34[rank], ["Clabel", "conductor", "ainvs", "rank", "torsion"])

    # cross-check with the LMFDB API list, if present
    p = os.path.join(DATA, "lmfdb_rank_ge2_sha_ne1_N_lt_500000.json")
    if os.path.exists(p):
        api = json.load(open(p))["data"]
        api_labels = sorted(r["Clabel"] for r in api if r.get("Clabel"))
        ec_labels = sorted(r["Clabel"] for r in big)
        log("cross-check: API list has %d curves, ecdata list has %d; identical label sets: %s"
            % (len(api_labels), len(ec_labels), api_labels == ec_labels))
        if api_labels != ec_labels:
            log("  only API:", sorted(set(api_labels) - set(ec_labels)))
            log("  only ecdata:", sorted(set(ec_labels) - set(api_labels)))


def conductor_of(label):
    """Conductor from a Cremona label such as '389a1' or '194040co6'."""
    digits = ""
    for ch in label:
        if not ch.isdigit():
            break
        digits += ch
    return int(digits)


def ecdata_bsd_lookup(labels):
    """Return {Clabel: {ainvs, rank, torsion, tamagawa, real_period, L1, regulator, sha}} from allbsd."""
    want = {}
    for lab in labels:
        want.setdefault(conductor_of(lab) // 10000, set()).add(lab)
    out = {}
    for idx, labs in want.items():
        chunk = ECDATA_CHUNKS[idx]
        path = ecdata_file("allbsd", chunk)
        with open(path) as f:
            for line in f:
                parts = line.split()
                if len(parts) < 10:
                    continue
                lab = parts[0] + parts[1] + parts[2]
                if lab in labs:
                    out[lab] = {"ainvs": parts[3], "rank": int(parts[4]), "torsion": int(parts[5]),
                                "tamagawa": int(parts[6]), "real_period": parts[7], "L1": parts[8],
                                "regulator": parts[9], "sha": parts[10]}
    return out


def ecdata_gens_lookup(labels):
    """{Clabel: [[x,y],...]} generators of infinite order from ecdata allgens
    (line format: ID AI R TOR <R points of infinite order> <torsion generators>, points as [X:Y:Z])."""
    want = {}
    for lab in labels:
        want.setdefault(conductor_of(lab) // 10000, set()).add(lab)
    out = {}
    for idx, labs in want.items():
        path = ecdata_file("allgens", ECDATA_CHUNKS[idx])
        with open(path) as f:
            for line in f:
                parts = line.split()
                if len(parts) < 5:
                    continue
                lab = parts[0] + parts[1] + parts[2]
                if lab in labs:
                    r = int(parts[4])
                    pts = []
                    for tok in parts[6:6 + r]:
                        X, Y, Z = [int(t) for t in tok.strip("[]").split(":")]
                        pts.append(["%d/%d" % (X, Z) if Z != 1 else str(X), "%d/%d" % (Y, Z) if Z != 1 else str(Y)])
                    out[lab] = pts
    return out


def task_picks():
    """The 10 rank-2 curves with Sha>1 of smallest conductor (< 500000), with generators (ecdata allgens)
    and BSD reference values (ecdata allbsd; LMFDB ec_mwbsd if the API answers)."""
    p = os.path.join(DATA, "lmfdb_rank_ge2_sha_ne1_N_lt_500000.json")
    if os.path.exists(p):
        recs = json.load(open(p))["data"]
        src = "LMFDB API (lmfdb_rank_ge2_sha_ne1_N_lt_500000.json)"
    else:
        recs = json.load(open(os.path.join(DATA, "ecdata_rank_ge2_sha_gt1_N_lt_500000.json")))["data"]
        src = "ecdata allbigsha"
    picks = [r for r in recs if r["rank"] == 2 and float(r["sha"]) > 1]
    picks.sort(key=lambda r: (r["conductor"], r["Clabel"]))
    picks = picks[:10]
    labels = [r["Clabel"] for r in picks]
    gens = ecdata_gens_lookup(labels)
    bsd = ecdata_bsd_lookup(labels)
    for r in picks:
        r["gens"] = gens.get(r["Clabel"], [])
        r["ecdata_bsd"] = bsd.get(r["Clabel"], {})
        if isinstance(r.get("ainvs"), str):
            r["ainvs"] = json.loads(r["ainvs"])
        try:
            if "lmfdb_label" in r:
                doc = api_get("ec_mwbsd", {"_format": "json", "lmfdb_label": "s" + r["lmfdb_label"]}, retries=1)
                mw = doc["data"][0] if doc["data"] else {}
                r["mwbsd"] = {k: real_literal(v) for k, v in mw.items() if k != "id"}
        except RuntimeError as e:
            log("  (ec_mwbsd unavailable for %s)" % r["Clabel"])
    write_json("lmfdb_rank2_sha_picks.json", {"meta": {"source": src, "date": time.strftime("%Y-%m-%d"),
                                                       "note": "10 rank-2 curves with sha>1 of smallest conductor"},
                                              "data": picks})
    path = os.path.join(DATA, "lmfdb_rank2_sha_picks.gp")
    with open(path, "w") as f:
        f.write("\\\\ generated by compute/scripts/lmfdb_rank2.py --picks\n")
        f.write("\\\\ entries: [Clabel, lmfdb_label, ainvs, sha (LMFDB/ecdata, rounded), conductor, generators]\n")
        f.write("{\nLMFDB_PICKS = [\n")
        for i, r in enumerate(picks):
            sep = "," if i < len(picks) - 1 else ""
            g = "[" + ",".join("[%s,%s]" % (x, y) for x, y in r["gens"]) + "]"
            f.write('  ["%s", "%s", %s, %d, %d, %s]%s\n' % (r["Clabel"], r.get("lmfdb_label", ""),
                                                           json.dumps(r["ainvs"]).replace(" ", ""), int(float(r["sha"])),
                                                           r["conductor"], g, sep))
        f.write("];\n}\n")
    log("wrote", path)


def task_ecdata_reference(labels):
    ref = ecdata_bsd_lookup(labels)
    write_json("ecdata_bsd_reference.json", {"meta": {"source": ECDATA_RAW + "allbsd/allbsd.<range>",
                                                      "fields": "ID AI R T CP OM L1 REG SHA (docs/file-format.txt)",
                                                      "date": time.strftime("%Y-%m-%d")}, "data": ref})
    return ref


def task_compare(tsv_path):
    """Compare rank, analytic Sha, L^(r)(E,1)/r!, Omega_E and the regulator from bsd_table.gp (TSV) with the
    reference data: LMFDB ec_curvedata (`rank`, `sha` = analytic Sha rounded) and ec_mwbsd (if fetched), and
    Cremona's ecdata allbsd (R T CP OM L1 REG SHA; identical source for N <= 500000)."""
    ref = {}
    p = os.path.join(DATA, "ecdata_bsd_reference.json")
    if os.path.exists(p):
        for k, v in json.load(open(p))["data"].items():
            ref[k] = {"rank": v["rank"], "sha": float(v["sha"]), "L1": v["L1"], "period": v["real_period"],
                      "reg": v["regulator"], "src": "ecdata allbsd", "lmfdb_label": ""}
    p = os.path.join(DATA, "lmfdb_bsd_reference.json")
    if os.path.exists(p):
        for k, v in json.load(open(p))["data"].items():
            cd, mw = v["curvedata"], v.get("mwbsd", {})
            ref[k] = {"rank": cd["rank"], "sha": float(cd["sha"]), "L1": mw.get("special_value", "?"),
                      "period": mw.get("real_period", "?"), "reg": cd.get("regulator", "?"), "src": "LMFDB API",
                      "lmfdb_label": cd["lmfdb_label"]}
    p = os.path.join(DATA, "lmfdb_rank2_sha_picks.json")
    if os.path.exists(p):
        for r in json.load(open(p))["data"]:
            eb = r.get("ecdata_bsd", {})
            ref[r["Clabel"]] = {"rank": r["rank"], "sha": float(r["sha"]), "L1": eb.get("L1", "?"),
                                "period": eb.get("real_period", "?"), "reg": eb.get("regulator", "?"),
                                "src": "LMFDB API `sha`/`rank` + ecdata allbsd", "lmfdb_label": r.get("lmfdb_label", "")}
    rows = list(csv.DictReader(open(tsv_path), delimiter="\t"))
    print("| curve | LMFDB label | r_alg ours | r_alg ref | Sha_an ours (60 digits, shown 15) | Sha ref | L^(r)/r! ref (15 digits) | Omega_E ref | Reg ref | source | agree |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    nagree = 0
    for r in rows:
        lab = r["label"]
        rr = ref.get(lab)
        r_alg = r["r_lower"] if r["rank_certified"] == "yes" else "%s..%s" % (r["r_lower"], r["r_upper"])
        ours = float(r["sha_an"])
        if rr is None:
            print(f"| {lab} | {r['lmfdb_label']} | {r_alg} | ? | {ours:.15f} | ? | ? | ? | ? | none | ? |")
            continue
        ok = abs(ours - rr["sha"]) < 1e-9 and str(rr["rank"]) == r["r_lower"]
        # numerical agreement of L1, period, regulator with the 15-digit reference values
        def close(a, b):
            try:
                return abs(float(a) - float(b)) <= 2e-14 * max(1.0, abs(float(b)))
            except (TypeError, ValueError):
                return None
        ok_num = [close(r["L_r_over_rfact"], rr["L1"]), close(r["Omega_E"], rr["period"]), close(r["regulator"], rr["reg"])]
        ok_all = ok and all(x is not False for x in ok_num)
        nagree += ok_all
        print(f"| {lab} | {rr['lmfdb_label'] or r['lmfdb_label']} | {r_alg} | {rr['rank']} | {ours:.15f} | {rr['sha']:g} | "
              f"{rr['L1']} | {rr['period']} | {rr['reg']} | {rr['src']} | {'yes' if ok_all else 'NO ' + str(ok_num)} |")
    print(f"\n{nagree} of {len(rows)} curves: rank, analytic Sha (to 1e-9), L^(r)(E,1)/r!, Omega_E and regulator "
          f"(to 15 digits) agree with the reference.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fields", action="store_true")
    ap.add_argument("--sha", action="store_true")
    ap.add_argument("--rank34", action="store_true")
    ap.add_argument("--counts", action="store_true")
    ap.add_argument("--reference", action="store_true")
    ap.add_argument("--ecdata", action="store_true",
                    help="counts/lists from Cremona's ecdata files (cached in .tools/ecdata)")
    ap.add_argument("--picks", action="store_true",
                    help="10 rank-2 curves with Sha>1 of smallest conductor, with generators -> lmfdb_rank2_sha_picks.{json,gp}")
    ap.add_argument("--ecdata-reference", metavar="LABELS",
                    help="comma-separated Cremona labels: BSD reference values from ecdata allbsd files")
    ap.add_argument("--compare", metavar="TSV")
    ap.add_argument("--all", action="store_true", help="fields, sha, rank34, reference, ecdata (not the slow API --counts)")
    a = ap.parse_args()
    os.makedirs(DATA, exist_ok=True)
    t0 = time.time()
    if a.fields or a.all:
        task_fields()
    if a.sha or a.all:
        task_sha()
    if a.rank34 or a.all:
        task_rank34()
    if a.reference or a.all:
        task_reference(BSD_TABLE_CURVES)
    if a.ecdata or a.all:
        task_ecdata()
    if a.picks or a.all:
        task_picks()
    if a.ecdata_reference:
        task_ecdata_reference(a.ecdata_reference.split(","))
    if a.counts:
        task_counts()
    if a.compare:
        task_compare(a.compare)
    log(f"done: {NREQ} API requests in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
