# IP Knowledge Layer data-20260629-162606Z

Automated data release generated at `2026-06-29T16:26:06Z`.

GitHub Release: [data-20260629-162606Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20260629-162606Z)

## Highlights

- 135,083 normalized knowledge records
- 135,083 prefix records
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
| `hosting-cloud` | 102,209 |
| `satellite-internet` | 14,121 |
| `anonymity` | 11,448 |
| `crawler-bot` | 7,305 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 76,120 |
| AWS | 16,380 |
| Tor | 11,448 |
| GitHub | 7,469 |
| starlink | 5,865 |
| viasat | 4,547 |
| The Trade Desk | 2,615 |
| Amazon | 2,059 |
| Oracle Cloud | 1,089 |
| Google Cloud | 996 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 76,120 |
| `aws` | 16,380 |
| `sat-geoip` | 14,121 |
| `tor-radar` | 11,448 |
| `github-meta` | 7,469 |
| `crawler-scope` | 7,305 |
| `oracle-cloud` | 1,089 |
| `gcp-cloud` | 996 |
| `gcp-goog` | 112 |
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
