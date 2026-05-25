# IP Knowledge Layer data-20260525-143612Z

Automated data release generated at `2026-05-25T14:36:12Z`.

GitHub Release: [data-20260525-143612Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20260525-143612Z)

## Highlights

- 122,739 normalized knowledge records
- 122,739 prefix records
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
| `hosting-cloud` | 98,192 |
| `anonymity` | 11,493 |
| `satellite-internet` | 11,232 |
| `crawler-bot` | 1,822 |

## Top Providers

| Provider | Records |
|---|---:|
| Azure | 73,422 |
| AWS | 15,868 |
| Tor | 11,493 |
| GitHub | 6,703 |
| starlink | 5,407 |
| viasat | 4,523 |
| Oracle Cloud | 1,078 |
| Google Cloud | 967 |
| hughes | 675 |
| Google | 449 |

## Sources

| Source | Records |
|---|---:|
| `azure` | 73,422 |
| `aws` | 15,868 |
| `tor-radar` | 11,493 |
| `sat-geoip` | 11,232 |
| `github-meta` | 6,703 |
| `crawler-scope` | 1,822 |
| `oracle-cloud` | 1,078 |
| `gcp-cloud` | 967 |
| `gcp-goog` | 111 |
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
