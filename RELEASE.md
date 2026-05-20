# IP Knowledge Layer v0.1.0

Initial data-first release.

## Highlights

- 113,349 normalized knowledge records
- 111,419 prefix records
- 97,973 official cloud/CDN/developer-platform records
- 11,615 Tor relay host-route records
- 1,831 crawler/bot/monitoring/scanner records from CrawlerScope
- 1,930 VPN-adjacent ASN aggregate signals
- 12 sources
- 0 collector errors in the current build

## Files To Pull

```bash
BASE="https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current"

curl -fsSLO "$BASE/summary.json"
curl -fsSLO "$BASE/source-index.json"
curl -fsSLO "$BASE/ip-knowledge.jsonl"
curl -fsSLO "$BASE/ip-knowledge.csv"
curl -fsSLO "$BASE/cloud-prefixes.csv"
curl -fsSLO "$BASE/asn-signals.csv"
curl -fsSLO "$BASE/cidr-tags.txt"
```

## Current Files

```text
data/current/summary.json
data/current/source-index.json
data/current/ip-knowledge.jsonl
data/current/ip-knowledge.csv
data/current/cloud-prefixes.csv
data/current/asn-signals.csv
data/current/cidr-tags.txt
data/history/summary.csv
data/snapshots/*.json
```

## Sources

Official cloud/CDN/developer-platform sources:

- AWS
- Azure
- Google Cloud
- Google public infrastructure
- Cloudflare
- Fastly
- GitHub
- Oracle Cloud

Derived ipanalytics sources:

- CrawlerScope
- Tor-Radar
- VPN provider ASN summary

## Improvements Over Simple IP Lists

- Normalized record shape across cloud, crawler, Tor, and ASN-signal sources
- Source provenance per record
- Source-level confidence
- Operational tags such as `cloud`, `cdn`, `edge`, `crawler`, `ai-crawler`,
  `tor-exit`, and `vpn-adjacent`
- Compact historical snapshots to avoid repository bloat
- No full IPv4 expansion
- No raw VPN IP feed publication

## Planned Next

- `asn-knowledge.csv`
- `asn-prefixes.csv.gz`
- provider alias normalization
- overlap summaries between layers
- added/removed prefix diffs
