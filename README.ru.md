_English version: [README.md](README.md)_

# IP Knowledge Layer

Открытый слой знаний для обогащения IP-данных (IP enrichment): сетевая разведка (network intelligence) по CIDR, ASN, облакам, краулерам, Tor и смежным с VPN сетям.
Также включает данные о префиксах спутникового интернета, полученные из публичных GeoIP-фидов операторов, сопоставления подсеть–PoP, свидетельства BGP и сигналы владения.

<p align="center">
  <img src="./site/banner.png" alt="Open IP enrichment knowledge layer for CIDR, ASN, cloud, crawler, Tor, and
VPN-adjacent network intelligence." width="100%">
</p>

Этот репозиторий ориентирован на данные (data-first): основной результат работы — набор машиночитаемых файлов, которые можно забирать напрямую через `curl`, GitHub Actions, SIEM-конвейеры, WAF-инструменты, антифрод-системы и внутренние задачи по обогащению данных.



## Зачем это существует

Большинство публичных IP-репозиториев публикуют один узкий список: облачные IP, IP Tor, IP краулеров или сопоставления ASN. IP Knowledge Layer объединяет несколько публичных и производных сигналов в один нормализованный слой обогащения.

Ценность — в контексте:

```text
CIDR or ASN -> layer -> provider -> service -> tags -> confidence -> source
```

Вместо того чтобы лишь знать о существовании префикса, потребители данных могут понять, принадлежит ли он облачному хостингу, edge-инфраструктуре CDN, инфраструктуре GitHub, AI-краулерам, Tor, провайдеру спутникового интернета или является VPN-смежным сигналом ASN.

## Текущий релиз

<!-- IPKL_SUMMARY_START -->
| Метрика | Значение |
|---|---:|
| Обновлено | `2026-09-12T15:46:43Z` |
| Релиз | [data-20260912-154643Z](https://github.com/ipanalytics/IP-Knowledge-Layer/releases/tag/data-20260912-154643Z) |
| Записей | 125,758 |
| Записей префиксов | 125,758 |
| ASN-сигналов | 0 |
| Источников | 12 |
| Ошибок сборщика | 1 |

| Слой | Записей |
|---|---:|
| `hosting-cloud` | 91,115 |
| `satellite-internet` | 15,285 |
| `anonymity` | 10,770 |
| `crawler-bot` | 8,588 |

| Крупнейшие провайдеры | Записей |
|---|---:|
| Azure | 64,131 |
| AWS | 17,438 |
| Tor | 10,770 |
| GitHub | 7,148 |
| starlink | 6,549 |
<!-- IPKL_SUMMARY_END -->

## URL для скачивания

При необходимости замените `main` на другую ветку.

```bash
BASE="https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current"

curl -fsSL "$BASE/summary.json"
curl -fsSL "$BASE/source-index.json"
curl -fsSL "$BASE/ip-knowledge.jsonl"
curl -fsSL "$BASE/ip-knowledge.csv"
curl -fsSL "$BASE/cloud-prefixes.csv"
curl -fsSL "$BASE/asn-signals.csv"
curl -fsSL "$BASE/cidr-tags.txt"
```

## Какой файл использовать?

| Потребность | Используйте этот файл | Почему |
|---|---|---|
| Нужен полный слой знаний | `ip-knowledge.jsonl` | Лучше всего подходит для конвейеров, `jq`, потоковой обработки и сохранения вложенных полей |
| Нужны данные, удобные для Excel/BI/SIEM | `ip-knowledge.csv` | Тот же обширный набор данных в табличной форме |
| Нужны только диапазоны cloud/CDN/платформ разработки | `cloud-prefixes.csv` | Меньше по объёму и сфокусирован на AWS, Azure, GCP, Cloudflare, Fastly, GitHub, Oracle |
| Нужен быстрый поиск CIDR→теги | `cidr-tags.txt` | Лёгкий текстовый файл: один CIDR и теги через запятую в каждой строке |
| Важны ASN-сигналы провайдеров с высокой долей VPN | `asn-signals.csv` | Агрегированные свидетельства на уровне ASN без публикации сырых VPN IP |
| Нужно проверить состояние источников и счётчики | `summary.json` | Статус текущего запуска, счётчики по слоям, агрегаты по провайдерам/источникам |
| Нужны данные о происхождении источников | `source-index.json` | URL источников, типы источников и количество записей |

Для большинства пользователей:

```text
Start with cloud-prefixes.csv if you only need cloud/datacenter/CDN ranges.
Start with ip-knowledge.jsonl if you want the full enrichment layer.
Start with cidr-tags.txt if you want the simplest possible feed.
```

## Файлы

| Файл | Назначение | Примерный размер |
|---|---:|---:|
| `data/current/summary.json` | Сводка текущей сборки, счётчики, агрегаты по слоям/провайдерам/источникам | 8 KB |
| `data/current/source-index.json` | Метаданные источников, URL, типы источников, количество записей | 3 KB |
| `data/current/ip-knowledge.jsonl` | Полный нормализованный слой знаний, одна JSON-запись на строку | 49 MB |
| `data/current/ip-knowledge.csv` | Полный нормализованный слой знаний в формате CSV | 25 MB |
| `data/current/cloud-prefixes.csv` | Только официальные префиксы cloud/CDN/платформ разработки | 22 MB |
| `data/current/asn-signals.csv` | Агрегированные VPN-смежные сигналы на уровне ASN | 399 KB |
| `data/current/cidr-tags.txt` | Простой текстовый файл `CIDR tags` для лёгких потребителей | 4.7 MB |
| `data/history/summary.csv` | История сборок | небольшой |
| `data/snapshots/*.json` | Компактные сводные снимки, не полные копии данных | небольшой |

## Слои

### `hosting-cloud`

Официальные диапазоны IP облачных провайдеров, CDN, edge-инфраструктуры и платформ разработки.

Текущие провайдеры:

- AWS
- Azure
- Google Cloud
- Публичная инфраструктура Google
- Cloudflare
- Fastly
- GitHub
- Oracle Cloud

### `crawler-bot`

Диапазоны краулеров, AI-ботов, зондов мониторинга, сканеров, SEO-ботов и ботов социальных превью, полученные из [CrawlerScope](https://github.com/ipanalytics/CrawlerScope).

### `anonymity`

Маршруты хостов реле Tor, полученные из [Tor-Radar](https://github.com/ipanalytics/Tor-Radar).

### `satellite-internet`

Префиксы спутникового интернета и провайдеров спутниковых услуг, полученные из
[Sat-geoip](https://github.com/ipanalytics/Sat-geoip). Записи сохраняют оператора,
класс орбиты, состояние BGP, семантику GeoIP, назначение PoP и свидетельства уровня
доверия в поле `metrics` в формате JSONL.

### `asn-signal`

Агрегированные сигналы уровня ASN, смежные с VPN, на основе анализа провайдеров. Этот слой не
публикует сырые списки VPN IP. Он публикует только агрегированные свидетельства привязки
провайдеров к ASN.

## Перечень источников

Официальные/публичные источники:

- Диапазоны IP AWS: `https://ip-ranges.amazonaws.com/ip-ranges.json`
- Azure Service Tags: `https://www.microsoft.com/en-us/download/details.aspx?id=56519`
- Диапазоны Google Cloud: `https://www.gstatic.com/ipranges/cloud.json`
- Публичные диапазоны Google: `https://www.gstatic.com/ipranges/goog.json`
- Диапазоны Cloudflare: `https://www.cloudflare.com/ips-v4`, `https://www.cloudflare.com/ips-v6`
- Список публичных IP Fastly: `https://api.fastly.com/public-ip-list`
- GitHub Meta API: `https://api.github.com/meta`
- Диапазоны Oracle Cloud: `https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json`

Источники производных проектов:

- CrawlerScope: диапазоны краулеров, AI-ботов, систем мониторинга, сканеров и SEO-ботов
- Tor-Radar: IP ретрансляторов и выходных узлов Tor
- Sat-geoip: префиксы спутникового интернета, атрибуция операторов, свидетельства BGP/PoP/GeoIP
- VPN provider ASN summary: агрегированные ASN-сигналы, без сырого фида VPN IP

## Структура записи

Пример JSONL-записи `hosting-cloud`:

```json
{"prefix":"104.16.0.0/13","layer":"hosting-cloud","provider":"Cloudflare","service":"edge","tags":["cdn","edge","proxy"],"confidence":0.99,"source_id":"cloudflare-v4"}
```

Пример JSONL-записи `crawler-bot`:

```json
{"prefix":"66.249.64.0/19","layer":"crawler-bot","provider":"Google","service":"Google common crawlers","tags":["bot","crawler","search"],"confidence":0.95,"source_id":"crawler-scope"}
```

Пример JSONL-записи `anonymity`:

```json
{"prefix":"185.220.101.1/32","layer":"anonymity","provider":"Tor","service":"exit","tags":["anonymity-network","tor","tor-exit"],"confidence":0.98,"source_id":"tor-radar"}
```

Пример JSONL-записи `satellite-internet`:

```json
{"prefix":"143.105.187.0/24","layer":"satellite-internet","provider":"starlink","service":"satellite_internet","tags":["satellite","satellite-internet","leo","bgp_announced"],"confidence":0.985,"source_id":"sat-geoip"}
```

Пример JSONL-записи `asn-signal`:

```json
{"layer":"asn-signal","provider":"NordVPN","asn":9009,"asn_name":"M247","tags":["asn-signal","vpn-adjacent"],"confidence":0.7}
```

## Примеры использования

Получить текущую статистику сборки:

```bash
curl -fsSL https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/summary.json | jq .
```

Скачать облачные префиксы:

```bash
curl -fsSLO https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/cloud-prefixes.csv
```

Извлечь строки Cloudflare:

```bash
curl -fsSL https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/cloud-prefixes.csv \
  | awk -F, '$3 == "Cloudflare" { print }'
```

Извлечь выходные узлы Tor из JSONL:

```bash
curl -fsSL https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/ip-knowledge.jsonl \
  | jq -r 'select(.layer=="anonymity" and .service=="exit") | .prefix'
```

Извлечь префиксы AI-краулеров:

```bash
curl -fsSL https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/ip-knowledge.jsonl \
  | jq -r 'select(.layer=="crawler-bot" and (.tags | index("ai-crawler"))) | .prefix'
```

Использовать как лёгкий фид обогащения для блокировки/разрешения:

```bash
curl -fsSL https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/cidr-tags.txt \
  | grep 'cloud'
```

Найти все ASN-сигналы для провайдера:

```bash
curl -fsSL https://raw.githubusercontent.com/ipanalytics/IP-Knowledge-Layer/main/data/current/asn-signals.csv \
  | awk -F, '$3 == "NordVPN" { print }'
```

## Чем может помочь

- Обогащение данных об IP для систем антифрода/оценки рисков
- Контекст для WAF и SIEM
- Определение принадлежности к облаку/датацентру
- Классификация инфраструктуры CDN/edge
- Видимость AI-краулеров и ботов
- Контекст ретрансляторов Tor
- Сигналы уровня ASN, смежные с VPN
- Происхождение источников для объяснимых решений
- Построение внутренних списков разрешения, блокировки и очередей на проверку

Этот проект не является чёрным списком вредоносного ПО или злоупотреблений. Он предоставляет
операционный сетевой контекст с указанием происхождения источников и уровня доверия.

## Локальное обновление

```bash
python3 scripts/update.py
```

Сборщик предпочитает локальные выходные данные соседних проектов, если они присутствуют:

```text
../crawler-scope/data/current/crawlers.json
../tor-radar/data/current/network.json
../release/analysis/data/provider_asn.csv
```

Когда этих файлов нет, он по возможности загружает публичные raw-выходные данные проектов
с GitHub.

## GitHub Actions

Рабочий процесс (workflow) запускается каждые 6 часов и коммитит обновлённые файлы в `data/`.

```text
.github/workflows/ip-knowledge-layer.yml
```

Рабочий процесс намеренно хранит полные данные только в `data/current/*`. Исторические снимки представляют собой компактные сводки во избежание разрастания репозитория.

## Планируемые улучшения

Планируемые дополнения, вдохновлённые такими проектами, как `ipverse`:

- `asn-knowledge.csv`: сводные данные на уровне ASN с тегами, присутствием в облаках, присутствием Tor, присутствием краулеров, признаками VPN-смежности (VPN-adjacent) и уровнем достоверности.
- `asn-prefixes.csv.gz`: сжатый массовый слой сопоставления ASN с префиксами, хранящийся отдельно от `ip-knowledge.jsonl`, чтобы основной файл не становился слишком большим.
- `provider-index.json`: нормализованные метаданные провайдеров и псевдонимы.
- `overlap-summary.csv`: пересечения между сигналами ASN облачных сервисов/CDN, краулеров, Tor и признаками VPN-смежности.
- `diff/current.json`: сводка добавленных/удалённых префиксов между запусками.

Замысел не в том, чтобы клонировать `ipverse`. Цель — построить слой знаний более высокого уровня с указанием происхождения из источников (provenance), тегами и уровнем достоверности.

## Примечания

- Проект избегает полного развёртывания (expansion) IPv4.
- Проект избегает массовых RDAP/whois-запросов в GitHub Actions.
- Сигналы `vpn-adjacent` — это агрегированные индикаторы на уровне ASN, а не сырой дамп VPN IP-адресов.
- Достоверность — это достоверность на уровне источника, а не утверждение о том, что трафик из сети является вредоносным.
- Некоторые официальные провайдеры публикуют пересекающиеся строки сервисов для одного и того же префикса. Эти строки сохраняются, поскольку метки сервисов несут полезный контекст.

## Лицензия

CC0-1.0. См. `LICENSE`.
