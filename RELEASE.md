# IP Knowledge Layer data-20260803-152704Z

Automated data release generated at `2026-08-03T15:27:04Z`.

GitHub Release: [data-20260803-152704Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20260803-152704Z)

## Highlights

- 136,860 normalized knowledge records
- 136,860 prefix records
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
| `hosting-cloud` | 102,886 |
| `satellite-internet` | 14,613 |
| `anonymity` | 11,846 |
| `crawler-bot` | 7,515 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 76,573 |
| AWS | 16,564 |
| Tor | 11,846 |
| GitHub | 7,445 |
| starlink | 6,241 |
| viasat | 4,664 |
| The Trade Desk | 2,615 |
| Amazon | 2,059 |
| Oracle Cloud | 1,102 |
| Google Cloud | 1,045 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 76,573 |
| `aws` | 16,564 |
| `sat-geoip` | 14,613 |
| `tor-radar` | 11,846 |
| `crawler-scope` | 7,515 |
| `github-meta` | 7,445 |
| `oracle-cloud` | 1,102 |
| `gcp-cloud` | 1,045 |
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
