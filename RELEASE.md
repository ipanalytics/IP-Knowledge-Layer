# IP Knowledge Layer data-20260809-073657Z

Automated data release generated at `2026-08-09T07:36:57Z`.

GitHub Release: [data-20260809-073657Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20260809-073657Z)

## Highlights

- 138,260 normalized knowledge records
- 138,260 prefix records
- 0 ASN signals
- 12 sources
- 1 collector errors

## Files To Pull

The same files are committed under `data/current` and attached to the GitHub Release for this run.

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

| File | Direct URL |
|---|---|
| `data/current/summary.json` | [`summary.json`](https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/summary.json) |
| `data/current/source-index.json` | [`source-index.json`](https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/source-index.json) |
| `data/current/ip-knowledge.jsonl` | [`ip-knowledge.jsonl`](https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/ip-knowledge.jsonl) |
| `data/current/ip-knowledge.csv` | [`ip-knowledge.csv`](https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/ip-knowledge.csv) |
| `data/current/cloud-prefixes.csv` | [`cloud-prefixes.csv`](https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/cloud-prefixes.csv) |
| `data/current/asn-signals.csv` | [`asn-signals.csv`](https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/asn-signals.csv) |
| `data/current/cidr-tags.txt` | [`cidr-tags.txt`](https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/cidr-tags.txt) |

## Layers

| Layer | Records |
|---|---:|
| `hosting-cloud` | 104,294 |
| `satellite-internet` | 14,638 |
| `anonymity` | 11,858 |
| `crawler-bot` | 7,470 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 77,793 |
| AWS | 16,703 |
| Tor | 11,858 |
| GitHub | 7,445 |
| starlink | 6,263 |
| viasat | 4,664 |
| The Trade Desk | 2,615 |
| Amazon | 2,059 |
| Oracle Cloud | 1,102 |
| Google Cloud | 1,094 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 77,793 |
| `aws` | 16,703 |
| `sat-geoip` | 14,638 |
| `tor-radar` | 11,858 |
| `crawler-scope` | 7,470 |
| `github-meta` | 7,445 |
| `oracle-cloud` | 1,102 |
| `gcp-cloud` | 1,094 |
| `gcp-goog` | 114 |
| `fastly` | 21 |
| `cloudflare-v4` | 15 |
| `cloudflare-v6` | 7 |

## Collector Errors

| Collector | Error |
|---|---|
| `collect_vpn_asn` | `local VPN ASN summary not found; skipped in standalone runs` |

## Notes

- ASN signals are aggregate provider-to-ASN evidence, not raw VPN IP publication.
- Snapshot retention keeps compact summary snapshots only; full current data is in `data/current` and release assets.
