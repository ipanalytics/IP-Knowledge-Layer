# IP Knowledge Layer data-20261025-051158Z

Automated data release generated at `2026-10-25T05:11:58Z`.

GitHub Release: [data-20261025-051158Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20261025-051158Z)

## Highlights

- 134,181 normalized knowledge records
- 134,181 prefix records
- 0 ASN signals
- 11 sources
- 2 collector errors

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
| `hosting-cloud` | 98,901 |
| `satellite-internet` | 15,707 |
| `anonymity` | 10,954 |
| `crawler-bot` | 8,619 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 78,777 |
| AWS | 17,688 |
| Tor | 10,954 |
| starlink | 6,939 |
| viasat | 5,066 |
| Amazon | 3,131 |
| The Trade Desk | 2,615 |
| Google Cloud | 1,135 |
| Oracle Cloud | 1,107 |
| turksat | 1,003 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 78,777 |
| `aws` | 17,688 |
| `sat-geoip` | 15,707 |
| `tor-radar` | 10,954 |
| `crawler-scope` | 8,619 |
| `gcp-cloud` | 1,135 |
| `oracle-cloud` | 1,107 |
| `gcp-goog` | 148 |
| `fastly` | 24 |
| `cloudflare-v4` | 15 |
| `cloudflare-v6` | 7 |

## Collector Errors

| Collector | Error |
|---|---|
| `collect_github` | `HTTP Error 403: rate limit exceeded` |
| `collect_vpn_asn` | `local VPN ASN summary not found; skipped in standalone runs` |

## Notes

- ASN signals are aggregate provider-to-ASN evidence, not raw VPN IP publication.
- Snapshot retention keeps compact summary snapshots only; full current data is in `data/current` and release assets.
