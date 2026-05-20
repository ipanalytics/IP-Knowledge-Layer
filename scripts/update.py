#!/usr/bin/env python3
import csv
import hashlib
import ipaddress
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
DATA = ROOT / "data"
CURRENT = DATA / "current"
HISTORY = DATA / "history"
SNAPSHOTS = DATA / "snapshots"

USER_AGENT = os.environ.get(
    "IPKL_USER_AGENT",
    "IP-Knowledge-Layer/0.1 (+https://github.com/ipanalytics/IP-Knowledge-Layer; public-data collector)",
)
RETENTION_SNAPSHOTS = int(os.environ.get("IPKL_SNAPSHOT_RETENTION", "168"))
RETENTION_HISTORY_ROWS = int(os.environ.get("IPKL_HISTORY_RETENTION", "720"))

RAW_BASE = "https://raw.githubusercontent.com/ipanalytics"


SOURCES = {
    "aws": {
        "type": "official_json",
        "url": "https://ip-ranges.amazonaws.com/ip-ranges.json",
        "tags": ["cloud", "hosting", "datacenter"],
        "confidence": 0.99,
    },
    "gcp-cloud": {
        "type": "official_json",
        "url": "https://www.gstatic.com/ipranges/cloud.json",
        "tags": ["cloud", "hosting", "datacenter"],
        "confidence": 0.99,
    },
    "gcp-goog": {
        "type": "official_json",
        "url": "https://www.gstatic.com/ipranges/goog.json",
        "tags": ["google", "internet-platform"],
        "confidence": 0.97,
    },
    "cloudflare-v4": {
        "type": "official_text",
        "url": "https://www.cloudflare.com/ips-v4",
        "tags": ["cdn", "edge", "proxy"],
        "confidence": 0.99,
    },
    "cloudflare-v6": {
        "type": "official_text",
        "url": "https://www.cloudflare.com/ips-v6",
        "tags": ["cdn", "edge", "proxy"],
        "confidence": 0.99,
    },
    "azure": {
        "type": "official_json",
        "url": "https://www.microsoft.com/en-us/download/details.aspx?id=56519",
        "tags": ["cloud", "hosting", "datacenter"],
        "confidence": 0.99,
    },
    "fastly": {
        "type": "official_json",
        "url": "https://api.fastly.com/public-ip-list",
        "tags": ["cdn", "edge"],
        "confidence": 0.99,
    },
    "github-meta": {
        "type": "official_json",
        "url": "https://api.github.com/meta",
        "tags": ["developer-platform", "git-hosting", "ci"],
        "confidence": 0.98,
    },
    "oracle-cloud": {
        "type": "official_json",
        "url": "https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json",
        "tags": ["cloud", "hosting", "datacenter"],
        "confidence": 0.99,
    },
    "crawler-scope": {
        "type": "derived_project",
        "url": f"{RAW_BASE}/CrawlerScope/main/data/current/crawlers.json",
        "local": WORKSPACE / "crawler-scope" / "data" / "current" / "crawlers.json",
        "tags": ["crawler", "bot"],
        "confidence": 0.95,
    },
    "tor-radar": {
        "type": "derived_project",
        "url": f"{RAW_BASE}/Tor-Radar/main/data/current/network.json",
        "local": WORKSPACE / "tor-radar" / "data" / "current" / "network.json",
        "tags": ["tor", "anonymity-network"],
        "confidence": 0.98,
    },
    "vpn-asn-summary": {
        "type": "local_project",
        "url": "https://github.com/ipanalytics/ASN-VPN-Network-Intelligence",
        "local": WORKSPACE / "release" / "analysis" / "data" / "provider_asn.csv",
        "tags": ["vpn-adjacent", "asn-signal"],
        "confidence": 0.70,
    },
}


def request(url, timeout=90):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json,text/plain,*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def fetch_json(url):
    return json.loads(request(url).decode("utf-8", "replace"))


def fetch_text(url):
    return request(url).decode("utf-8", "replace")


def read_json(path):
    with path.open() as f:
        return json.load(f)


def load_json_source(source):
    local = source.get("local")
    if local and Path(local).exists():
        return read_json(Path(local)), None
    try:
        return fetch_json(source["url"]), None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return None, str(exc)


def normalize_prefix(value):
    if not value:
        return None
    try:
        return str(ipaddress.ip_network(str(value).strip(), strict=False))
    except ValueError:
        return None


def ip_to_host_prefix(value):
    ip = ipaddress.ip_address(str(value).strip())
    return f"{ip}/32" if ip.version == 4 else f"{ip}/128"


def record(prefix, layer, provider, source_id, source_url, generated_at, **extra):
    norm = normalize_prefix(prefix)
    if not norm:
        return None
    base = {
        "prefix": norm,
        "layer": layer,
        "provider": provider,
        "service": extra.get("service"),
        "region": extra.get("region"),
        "country": extra.get("country"),
        "asn": extra.get("asn"),
        "asn_name": extra.get("asn_name"),
        "tags": sorted(set(extra.get("tags", []))),
        "confidence": extra.get("confidence", 0.5),
        "source_id": source_id,
        "source_url": source_url,
        "source_type": extra.get("source_type"),
        "updated_at": generated_at,
    }
    return base


def add(records, *args, **kwargs):
    item = record(*args, **kwargs)
    if item:
        records.append(item)


def collect_aws(records, generated_at):
    sid = "aws"
    source = SOURCES[sid]
    payload = fetch_json(source["url"])
    for row in payload.get("prefixes", []):
        add(
            records,
            row.get("ip_prefix"),
            "hosting-cloud",
            "AWS",
            sid,
            source["url"],
            generated_at,
            service=row.get("service"),
            region=row.get("region"),
            tags=source["tags"],
            confidence=source["confidence"],
            source_type=source["type"],
        )
    for row in payload.get("ipv6_prefixes", []):
        add(
            records,
            row.get("ipv6_prefix"),
            "hosting-cloud",
            "AWS",
            sid,
            source["url"],
            generated_at,
            service=row.get("service"),
            region=row.get("region"),
            tags=source["tags"],
            confidence=source["confidence"],
            source_type=source["type"],
        )


def collect_gcp(records, generated_at, sid, provider):
    source = SOURCES[sid]
    payload = fetch_json(source["url"])
    for row in payload.get("prefixes", []):
        prefix = row.get("ipv4Prefix") or row.get("ipv6Prefix")
        add(
            records,
            prefix,
            "hosting-cloud",
            provider,
            sid,
            source["url"],
            generated_at,
            service=row.get("service") or row.get("scope"),
            region=row.get("scope"),
            tags=source["tags"],
            confidence=source["confidence"],
            source_type=source["type"],
        )


def collect_cloudflare(records, generated_at):
    for sid in ("cloudflare-v4", "cloudflare-v6"):
        source = SOURCES[sid]
        for line in fetch_text(source["url"]).splitlines():
            add(
                records,
                line.strip(),
                "hosting-cloud",
                "Cloudflare",
                sid,
                source["url"],
                generated_at,
                service="edge",
                tags=source["tags"],
                confidence=source["confidence"],
                source_type=source["type"],
            )


def collect_azure(records, generated_at):
    sid = "azure"
    source = SOURCES[sid]
    page = fetch_text(source["url"])
    match = re.search(r"https://download\.microsoft\.com/download/[^\" ]+ServiceTags_Public_\d+\.json", page, re.I)
    if not match:
        raise ValueError("Azure ServiceTags_Public JSON link not found")
    json_url = match.group(0)
    payload = fetch_json(json_url)
    for item in payload.get("values", []):
        props = item.get("properties", {})
        service = props.get("systemService") or item.get("name")
        region = props.get("region")
        for prefix in props.get("addressPrefixes", []):
            add(
                records,
                prefix,
                "hosting-cloud",
                "Azure",
                sid,
                json_url,
                generated_at,
                service=service,
                region=region,
                tags=source["tags"],
                confidence=source["confidence"],
                source_type=source["type"],
            )


def collect_fastly(records, generated_at):
    sid = "fastly"
    source = SOURCES[sid]
    payload = fetch_json(source["url"])
    for prefix in payload.get("addresses", []) + payload.get("ipv6_addresses", []):
        add(
            records,
            prefix,
            "hosting-cloud",
            "Fastly",
            sid,
            source["url"],
            generated_at,
            service="edge",
            tags=source["tags"],
            confidence=source["confidence"],
            source_type=source["type"],
        )


def collect_github(records, generated_at):
    sid = "github-meta"
    source = SOURCES[sid]
    payload = fetch_json(source["url"])
    keys = ("hooks", "web", "api", "git", "packages", "pages", "importer", "actions", "dependabot")
    for key in keys:
        for prefix in payload.get(key, []) or []:
            add(
                records,
                prefix,
                "hosting-cloud",
                "GitHub",
                sid,
                source["url"],
                generated_at,
                service=key,
                tags=source["tags"],
                confidence=source["confidence"],
                source_type=source["type"],
            )


def collect_oracle(records, generated_at):
    sid = "oracle-cloud"
    source = SOURCES[sid]
    payload = fetch_json(source["url"])
    for region in payload.get("regions", []):
        region_name = region.get("region")
        for cidr in region.get("cidrs", []):
            add(
                records,
                cidr.get("cidr"),
                "hosting-cloud",
                "Oracle Cloud",
                sid,
                source["url"],
                generated_at,
                service=cidr.get("tags", ["cloud"])[0] if cidr.get("tags") else "cloud",
                region=region_name,
                tags=source["tags"],
                confidence=source["confidence"],
                source_type=source["type"],
            )


def collect_crawler_scope(records, generated_at):
    sid = "crawler-scope"
    source = SOURCES[sid]
    payload, error = load_json_source(source)
    if error or not payload:
        return error
    for service in payload.get("services", []):
        tags = set(source["tags"])
        tags.add(service.get("category", "crawler"))
        if service.get("category") == "ai":
            tags.add("ai-crawler")
        for prefix in service.get("prefixes", {}).get("ipv4", []) + service.get("prefixes", {}).get("ipv6", []):
            add(
                records,
                prefix,
                "crawler-bot",
                service.get("operator"),
                sid,
                source["url"],
                generated_at,
                service=service.get("service"),
                country=service.get("operatorCountry"),
                tags=tags,
                confidence=source["confidence"] if service.get("ipListAuthoritative") else 0.65,
                source_type=service.get("sourceType"),
            )
    return None


def collect_tor_radar(records, generated_at):
    sid = "tor-radar"
    source = SOURCES[sid]
    payload, error = load_json_source(source)
    if error or not payload:
        return error
    for relay in payload.get("relays", []):
        tags = set(source["tags"])
        role = relay.get("role")
        if role:
            tags.add(f"tor-{role}")
        for ip in relay.get("ips", []):
            try:
                prefix = ip_to_host_prefix(ip)
            except ValueError:
                continue
            add(
                records,
                prefix,
                "anonymity",
                "Tor",
                sid,
                source["url"],
                generated_at,
                service=role,
                country=relay.get("country"),
                asn=int(str(relay.get("asn", "")).replace("AS", "")) if relay.get("asn") else None,
                asn_name=relay.get("asName"),
                tags=tags,
                confidence=source["confidence"],
                source_type=source["type"],
            )
    return None


def collect_vpn_asn(records, generated_at):
    sid = "vpn-asn-summary"
    source = SOURCES[sid]
    local = Path(source["local"])
    if not local.exists():
        return "local VPN ASN summary not found; skipped in standalone runs"
    with local.open() as f:
        for row in csv.DictReader(f):
            try:
                asn = int(row["asn"])
            except (ValueError, KeyError):
                continue
            records.append(
                {
                    "prefix": None,
                    "layer": "asn-signal",
                    "provider": row.get("provider"),
                    "service": "vpn-provider-footprint",
                    "region": None,
                    "country": None,
                    "asn": asn,
                    "asn_name": row.get("asn_org"),
                    "tags": sorted(set(source["tags"])),
                    "confidence": source["confidence"],
                    "source_id": sid,
                    "source_url": source["url"],
                    "source_type": source["type"],
                    "updated_at": generated_at,
                    "metrics": {
                        "country_count": int(float(row.get("country_count") or 0)),
                        "ip_count": int(float(row.get("ip_count") or 0)),
                        "prefix_count": int(float(row.get("prefix_count") or 0)),
                        "hosting_ip_count": int(float(row.get("hosting_ip_count") or 0)),
                        "exit_node_count": int(float(row.get("exit_node_count") or 0)),
                        "avg_confidence": float(row.get("avg_confidence") or 0),
                    },
                }
            )
    return None


def stable_key(item):
    return "|".join(str(item.get(k) or "") for k in ("prefix", "layer", "provider", "service", "asn", "source_id"))


def dedupe(records):
    out = {}
    for item in records:
        out[stable_key(item)] = item
    return [out[key] for key in sorted(out)]


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w") as f:
        json.dump(value, f, indent=2, sort_keys=True)
        f.write("\n")
    tmp.replace(path)


def write_jsonl(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w") as f:
        for row in rows:
            f.write(json.dumps(row, sort_keys=True) + "\n")
    tmp.replace(path)


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            flat = dict(row)
            flat["tags"] = "|".join(row.get("tags", []))
            writer.writerow(flat)
    tmp.replace(path)


def append_summary(path, row):
    fields = ["generatedAt", "records", "prefixRecords", "asnSignals", "sources", "hostingCloud", "crawlerBot", "anonymity"]
    old = []
    if path.exists():
        with path.open() as f:
            old = list(csv.DictReader(f))
    old.append({key: row.get(key, "") for key in fields})
    old = old[-RETENTION_HISTORY_ROWS:]
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(old)


def fmt(value):
    return f"{int(value):,}"


def render_readme_summary(output):
    summary = output["summary"]
    layers = output["aggregates"]["layers"]
    providers = output["aggregates"]["providers"][:5]
    lines = [
        "<!-- IPKL_SUMMARY_START -->",
        "| Metric | Value |",
        "|---|---:|",
        f"| Updated | `{summary['generatedAt']}` |",
        f"| Records | {fmt(summary['records'])} |",
        f"| Prefix records | {fmt(summary['prefixRecords'])} |",
        f"| ASN signals | {fmt(summary['asnSignals'])} |",
        f"| Sources | {fmt(summary['sources'])} |",
        f"| Collector errors | {fmt(len(summary.get('errors', {})))} |",
        "",
        "| Layer | Records |",
        "|---|---:|",
    ]
    lines.extend(f"| `{row['key']}` | {fmt(row['count'])} |" for row in layers)
    lines.extend(["", "| Top Provider | Records |", "|---|---:|"])
    lines.extend(f"| {row['key']} | {fmt(row['count'])} |" for row in providers)
    lines.append("<!-- IPKL_SUMMARY_END -->")
    return "\n".join(lines)


def update_readme(output):
    path = ROOT / "README.md"
    if not path.exists():
        return
    text = path.read_text()
    start = "<!-- IPKL_SUMMARY_START -->"
    end = "<!-- IPKL_SUMMARY_END -->"
    if start not in text or end not in text:
        return
    before = text.split(start, 1)[0]
    after = text.split(end, 1)[1]
    path.write_text(before + render_readme_summary(output) + after)


def main():
    now = datetime.now(timezone.utc).replace(microsecond=0)
    generated_at = now.isoformat().replace("+00:00", "Z")
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    CURRENT.mkdir(parents=True, exist_ok=True)
    HISTORY.mkdir(parents=True, exist_ok=True)
    SNAPSHOTS.mkdir(parents=True, exist_ok=True)

    records = []
    errors = {}
    collectors = [
        collect_aws,
        lambda rows, ts: collect_gcp(rows, ts, "gcp-cloud", "Google Cloud"),
        lambda rows, ts: collect_gcp(rows, ts, "gcp-goog", "Google"),
        collect_cloudflare,
        collect_azure,
        collect_fastly,
        collect_github,
        collect_oracle,
    ]
    for fn in collectors:
        try:
            fn(records, generated_at)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError) as exc:
            errors[getattr(fn, "__name__", "collector")] = str(exc)

    for fn in (collect_crawler_scope, collect_tor_radar, collect_vpn_asn):
        error = fn(records, generated_at)
        if error:
            errors[fn.__name__] = error

    records = dedupe(records)
    prefix_records = [row for row in records if row.get("prefix")]
    asn_signals = [row for row in records if row.get("layer") == "asn-signal"]

    by_layer = Counter(row["layer"] for row in records)
    by_provider = Counter(row["provider"] for row in records)
    by_source = Counter(row["source_id"] for row in records)
    summary = {
        "generatedAt": generated_at,
        "records": len(records),
        "prefixRecords": len(prefix_records),
        "asnSignals": len(asn_signals),
        "sources": len(by_source),
        "hostingCloud": by_layer.get("hosting-cloud", 0),
        "crawlerBot": by_layer.get("crawler-bot", 0),
        "anonymity": by_layer.get("anonymity", 0),
        "errors": errors,
    }
    source_index = {}
    for source_id, meta in SOURCES.items():
        clean = {key: str(value) if isinstance(value, Path) else value for key, value in meta.items()}
        clean["records"] = by_source.get(source_id, 0)
        source_index[source_id] = clean
    output = {
        "generatedAt": generated_at,
        "summary": summary,
        "aggregates": {
            "layers": [{"key": k, "count": v} for k, v in by_layer.most_common()],
            "providers": [{"key": k, "count": v} for k, v in by_provider.most_common()],
            "sources": [{"key": k, "count": v} for k, v in by_source.most_common()],
        },
    }

    fields = ["prefix", "layer", "provider", "service", "region", "country", "asn", "asn_name", "tags", "confidence", "source_id", "source_url", "source_type", "updated_at"]
    write_json(CURRENT / "summary.json", output)
    write_json(CURRENT / "source-index.json", source_index)
    write_jsonl(CURRENT / "ip-knowledge.jsonl", records)
    write_csv(CURRENT / "ip-knowledge.csv", records, fields)
    write_csv(CURRENT / "cloud-prefixes.csv", [r for r in prefix_records if r["layer"] == "hosting-cloud"], fields)
    write_csv(CURRENT / "asn-signals.csv", asn_signals, fields)
    (CURRENT / "cidr-tags.txt").write_text(
        "\n".join(f"{row['prefix']} {','.join(row.get('tags', []))}" for row in prefix_records) + "\n"
    )
    write_json(SNAPSHOTS / f"{stamp}.json", output)
    append_summary(HISTORY / "summary.csv", summary)
    update_readme(output)

    snapshots = sorted(SNAPSHOTS.glob("*.json"))
    for path in snapshots[:-RETENTION_SNAPSHOTS]:
        path.unlink()
    print(f"generated records={len(records)} prefixes={len(prefix_records)} asn_signals={len(asn_signals)} errors={len(errors)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"update failed: {exc}", file=sys.stderr)
        sys.exit(1)
