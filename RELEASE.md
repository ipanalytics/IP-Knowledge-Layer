# IP Knowledge Layer data-20260922-171320Z

Automated data release generated at `2026-09-22T17:13:20Z`.

GitHub Release: [data-20260922-171320Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20260922-171320Z)

## Highlights

- 128,627 normalized knowledge records
- 128,627 prefix records
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
| `hosting-cloud` | 93,964 |
| `satellite-internet` | 15,280 |
| `anonymity` | 10,793 |
| `crawler-bot` | 8,590 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 66,620 |
| AWS | 17,464 |
| Tor | 10,793 |
| GitHub | 7,482 |
| starlink | 6,585 |
| viasat | 5,024 |
| Amazon | 3,131 |
| The Trade Desk | 2,615 |
| Oracle Cloud | 1,107 |
| Google Cloud | 1,103 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 66,620 |
| `aws` | 17,464 |
| `sat-geoip` | 15,280 |
| `tor-radar` | 10,793 |
| `crawler-scope` | 8,590 |
| `github-meta` | 7,482 |
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
