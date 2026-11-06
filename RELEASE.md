# IP Knowledge Layer data-20261106-193859Z

Automated data release generated at `2026-11-06T19:38:59Z`.

GitHub Release: [data-20261106-193859Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20261106-193859Z)

## Highlights

- 135,673 normalized knowledge records
- 135,673 prefix records
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
| `hosting-cloud` | 100,006 |
| `satellite-internet` | 15,755 |
| `anonymity` | 11,283 |
| `crawler-bot` | 8,629 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 71,164 |
| AWS | 17,794 |
| Tor | 11,283 |
| GitHub | 8,583 |
| starlink | 6,980 |
| viasat | 5,058 |
| Amazon | 3,131 |
| The Trade Desk | 2,615 |
| Google Cloud | 1,153 |
| Oracle Cloud | 1,118 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 71,164 |
| `aws` | 17,794 |
| `sat-geoip` | 15,755 |
| `tor-radar` | 11,283 |
| `crawler-scope` | 8,629 |
| `github-meta` | 8,583 |
| `gcp-cloud` | 1,153 |
| `oracle-cloud` | 1,118 |
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
