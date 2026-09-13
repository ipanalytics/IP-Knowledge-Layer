# IP Knowledge Layer data-20260913-121422Z

Automated data release generated at `2026-09-13T12:14:22Z`.

GitHub Release: [data-20260913-121422Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20260913-121422Z)

## Highlights

- 125,785 normalized knowledge records
- 125,785 prefix records
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
| `hosting-cloud` | 91,115 |
| `satellite-internet` | 15,286 |
| `anonymity` | 10,796 |
| `crawler-bot` | 8,588 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 64,131 |
| AWS | 17,438 |
| Tor | 10,796 |
| GitHub | 7,148 |
| starlink | 6,550 |
| viasat | 5,016 |
| Amazon | 3,131 |
| The Trade Desk | 2,615 |
| Oracle Cloud | 1,107 |
| Google Cloud | 1,103 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 64,131 |
| `aws` | 17,438 |
| `sat-geoip` | 15,286 |
| `tor-radar` | 10,796 |
| `crawler-scope` | 8,588 |
| `github-meta` | 7,148 |
| `oracle-cloud` | 1,107 |
| `gcp-cloud` | 1,103 |
| `gcp-goog` | 145 |
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
