# IP Knowledge Layer data-20260902-045923Z

Automated data release generated at `2026-09-02T04:59:23Z`.

GitHub Release: [data-20260902-045923Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20260902-045923Z)

## Highlights

- 124,547 normalized knowledge records
- 124,547 prefix records
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
| `hosting-cloud` | 90,455 |
| `satellite-internet` | 14,795 |
| `anonymity` | 11,795 |
| `crawler-bot` | 7,502 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 63,888 |
| AWS | 16,775 |
| Tor | 11,795 |
| GitHub | 7,399 |
| starlink | 6,386 |
| viasat | 4,692 |
| The Trade Desk | 2,615 |
| Amazon | 2,059 |
| Oracle Cloud | 1,107 |
| Google Cloud | 1,098 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 63,888 |
| `aws` | 16,775 |
| `sat-geoip` | 14,795 |
| `tor-radar` | 11,795 |
| `crawler-scope` | 7,502 |
| `github-meta` | 7,399 |
| `oracle-cloud` | 1,107 |
| `gcp-cloud` | 1,098 |
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
