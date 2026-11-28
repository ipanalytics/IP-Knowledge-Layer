# IP Knowledge Layer data-20261128-082103Z

Automated data release generated at `2026-11-28T08:21:03Z`.

GitHub Release: [data-20261128-082103Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20261128-082103Z)

## Highlights

- 146,142 normalized knowledge records
- 146,142 prefix records
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
| `hosting-cloud` | 109,152 |
| `satellite-internet` | 16,834 |
| `anonymity` | 11,415 |
| `crawler-bot` | 8,741 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 80,212 |
| AWS | 17,838 |
| starlink | 13,713 |
| Tor | 11,415 |
| GitHub | 8,634 |
| Amazon | 3,131 |
| The Trade Desk | 2,615 |
| Google Cloud | 1,153 |
| Oracle Cloud | 1,121 |
| DuckDuckGo | 968 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 80,212 |
| `aws` | 17,838 |
| `sat-geoip` | 16,834 |
| `tor-radar` | 11,415 |
| `crawler-scope` | 8,741 |
| `github-meta` | 8,634 |
| `gcp-cloud` | 1,153 |
| `oracle-cloud` | 1,121 |
| `gcp-goog` | 148 |
| `fastly` | 24 |
| `cloudflare-v4` | 15 |
| `cloudflare-v6` | 7 |

## Collector Errors

| Collector | Error |
|---|---|
| `collect_vpn_asn` | `local VPN ASN summary not found; skipped in standalone runs` |

## Notes

- ASN signals are aggregate provider-to-ASN evidence, not raw VPN IP publication.
- Snapshot retention keeps compact summary snapshots only; full current data is in `data/current` and release assets.
