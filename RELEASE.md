# IP Knowledge Layer data-20261002-060553Z

Automated data release generated at `2026-10-02T06:05:53Z`.

GitHub Release: [data-20261002-060553Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20261002-060553Z)

## Highlights

- 126,525 normalized knowledge records
- 126,525 prefix records
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
| `hosting-cloud` | 91,518 |
| `satellite-internet` | 15,370 |
| `anonymity` | 11,042 |
| `crawler-bot` | 8,595 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 64,396 |
| AWS | 17,466 |
| Tor | 11,042 |
| GitHub | 7,254 |
| starlink | 6,632 |
| viasat | 5,063 |
| Amazon | 3,131 |
| The Trade Desk | 2,615 |
| Google Cloud | 1,107 |
| Oracle Cloud | 1,107 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 64,396 |
| `aws` | 17,466 |
| `sat-geoip` | 15,370 |
| `tor-radar` | 11,042 |
| `crawler-scope` | 8,595 |
| `github-meta` | 7,254 |
| `gcp-cloud` | 1,107 |
| `oracle-cloud` | 1,107 |
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
