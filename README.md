
# IP Knowledge Layer


<p align="center">
  <img src="https://img.shields.io/badge/license-CC0--1.0-blue" alt="License">
  <img src="https://img.shields.io/github/actions/workflow/status/ipanalytics/IP-Knowledge-Layer/ip-knowledge-layer.yml?branch=main" alt="CI">
  <img src="https://img.shields.io/github/last-commit/ipanalytics/IP-Knowledge-Layer" alt="Last Commit">
  <img src="https://img.shields.io/github/repo-size/ipanalytics/IP-Knowledge-Layer" alt="Repo Size">
  <img src="https://img.shields.io/badge/dataset-active-success" alt="Dataset">
  <img src="https://img.shields.io/badge/format-jsonl%20%7C%20csv%20%7C%20txt-informational" alt="Formats">
</p>

---

Open IP enrichment knowledge layer for cloud infrastructure, crawler networks, Tor, ASN attribution, and VPN-adjacent network intelligence.

The repository publishes normalized machine-readable datasets intended for SIEM pipelines, fraud systems, enrichment services, gateways, analytics stacks, and operational network tooling.

Primary outputs:

* `ip-knowledge.jsonl`
* `ip-knowledge.csv`
* `cloud-prefixes.csv`
* `asn-signals.csv`
* `cidr-tags.txt`

---

## Overview

Most public IP datasets focus on a single domain:

* cloud ranges
* Tor exits
* crawler infrastructure
* ASN ownership
* VPN signals

IP Knowledge Layer consolidates those signals into a unified enrichment layer with normalized metadata, provider attribution, confidence scoring, and source provenance.

The goal is operational context.

```text
CIDR / ASN
    -> layer
    -> provider
    -> service
    -> tags
    -> confidence
    -> source
```

Instead of only identifying a prefix, consumers can classify infrastructure characteristics and attach explainable metadata to network events.

---

## Current Dataset Snapshot

| Metric           |   Value |
| ---------------- | ------: |
| Records          | 113,349 |
| Prefix records   | 111,419 |
| ASN signals      |   1,930 |
| Sources          |      12 |
| Collector errors |       0 |

### Layer Distribution

| Layer           | Records |
| --------------- | ------: |
| `hosting-cloud` |  97,973 |
| `anonymity`     |  11,615 |
| `asn-signal`    |   1,930 |
| `crawler-bot`   |   1,831 |

### Top Providers

| Provider     | Records |
| ------------ | ------: |
| Azure        |  73,422 |
| AWS          |  15,675 |
| Tor          |  11,615 |
| GitHub       |   6,677 |
| Oracle Cloud |   1,078 |

---

## Architecture

```text
                    Public Sources
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   Cloud Ranges      Crawler Feeds       Tor Signals
        │                  │                  │
        └──────────────┬───┴──────────────────┘
                       ▼
              Normalization Layer
              CIDR + metadata merge
                       ▼
               Attribution Engine
            provider / tags / confidence
                       ▼
                 Export Pipeline
        JSONL / CSV / TXT / summaries
                       ▼
              Operational Consumers
      SIEM / WAF / Fraud / Analytics
```

---

## Layers

### `hosting-cloud`

Official cloud, CDN, edge, and developer-platform infrastructure ranges.

Providers currently include:

* AWS
* Azure
* Google Cloud
* Cloudflare
* Fastly
* GitHub
* Oracle Cloud

---

### `crawler-bot`

Crawler, AI bot, monitoring, scanner, SEO, and preview infrastructure derived from:

* CrawlerScope

---

### `anonymity`

Tor relay and exit infrastructure derived from:

* Tor-Radar

---

### `asn-signal`

ASN-level VPN-adjacent aggregate attribution.

This layer intentionally publishes ASN evidence only, not raw VPN endpoint inventories.

---

## Files

| File                 | Description                               |
| -------------------- | ----------------------------------------- |
| `ip-knowledge.jsonl` | Full normalized enrichment layer          |
| `ip-knowledge.csv`   | Tabular export for analytics/SIEM tooling |
| `cloud-prefixes.csv` | Cloud/CDN/developer platform prefixes     |
| `asn-signals.csv`    | ASN-level VPN-adjacent signals            |
| `cidr-tags.txt`      | Lightweight CIDR-to-tags feed             |
| `summary.json`       | Build metadata and aggregate statistics   |
| `source-index.json`  | Source inventory and provenance           |

---

## Download

```bash
BASE="https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current"

curl -fsSLO "$BASE/ip-knowledge.jsonl"
curl -fsSLO "$BASE/cloud-prefixes.csv"
curl -fsSLO "$BASE/asn-signals.csv"
curl -fsSLO "$BASE/cidr-tags.txt"
```

---

## Record Format

Example JSONL record:

```json
{
  "prefix": "104.16.0.0/13",
  "layer": "hosting-cloud",
  "provider": "Cloudflare",
  "service": "edge",
  "tags": [
    "cdn",
    "edge",
    "proxy"
  ],
  "confidence": 0.99,
  "source_id": "cloudflare-v4"
}
```

---

## Usage Examples

### Extract Cloudflare prefixes

```bash
curl -fsSL "$BASE/cloud-prefixes.csv" \
  | awk -F, '$3 == "Cloudflare" { print }'
```

### Extract Tor exits

```bash
curl -fsSL "$BASE/ip-knowledge.jsonl" \
  | jq -r 'select(.layer=="anonymity" and .service=="exit") | .prefix'
```

### Extract AI crawler infrastructure

```bash
curl -fsSL "$BASE/ip-knowledge.jsonl" \
  | jq -r 'select(.tags | index("ai-crawler")) | .prefix'
```

### Find ASN signals for a provider

```bash
curl -fsSL "$BASE/asn-signals.csv" \
  | awk -F, '$3 == "NordVPN" { print }'
```

---

## Operational Use Cases

| Domain             | Usage                            |
| ------------------ | -------------------------------- |
| Fraud Detection    | VPN/Tor/datacenter scoring       |
| SIEM Enrichment    | Infrastructure attribution       |
| WAF Pipelines      | Cloud and crawler classification |
| Threat Hunting     | Network context correlation      |
| Bot Management     | AI crawler visibility            |
| Internal Analytics | Infrastructure intelligence      |

---

## Local Update

```bash
python3 scripts/update.py
```

Preferred local enrichment sources:

```text
../crawler-scope/data/current/crawlers.json
../tor-radar/data/current/network.json
../release/analysis/data/provider_asn.csv
```

If local datasets are unavailable, the collector falls back to public upstream sources.

---

## GitHub Actions

Dataset builds run every 6 hours.

```text
.github/workflows/ip-knowledge-layer.yml
```

Only current datasets are stored in full. Historical snapshots remain compact to avoid repository growth.

---

## Notes

* CIDRs are preserved without full IPv4 expansion
* Overlapping provider ranges are intentionally retained
* Confidence reflects source reliability, not maliciousness
* ASN VPN signals are aggregate indicators, not endpoint dumps
* The project avoids mass RDAP/WHOIS crawling during CI builds

---

## Roadmap

Planned additions:

* ASN rollup datasets
* Prefix overlap analysis
* Historical diff exports
* Provider metadata index
* Compressed ASN-to-prefix layers
* Confidence weighting improvements

---

## License

CC0-1.0. See [`LICENSE`](./LICENSE).

---

## Disclaimer

This repository publishes operational network enrichment data derived from public and derived infrastructure sources. Consumers are responsible for validating suitability within their own environments.
