# API
# BIDV Exchange Rate Scraper

A **Python Playwright** tool that monitors and extracts **foreign exchange rate data** from the official **BIDV website** by intercepting internal API (XHR / Fetch) responses.

Instead of scraping HTML, this project **captures JSON responses directly from the network layer** when the page loads.

---

### Projects Structure

API/
├── .venv/
├── report/
│ ├── report_exchange_rate.txt
│ └── report_gold_price.txt
├── api_login.py
├── data.py
├── get_cur_exchange_gold.py
├── get_cur_exchange_usd.py
├── pages.py
├── init.py
├── requirements.txt
├── uv.lock
└── README.md

## 🚀 Features

- Automatically opens BIDV exchange rate page using Chromium (headless)
- Listens to all network responses (XHR / Fetch)
- Filters responses with `Content-Type: application/json`
- Detects exchange rate API (`ExchangeDetailServlet`)
- Extracts and logs key information:
  - Update time
  - Currency code
  - Cash buying rate
- Logging powered by **loguru**

---

## 🛠 Tech Stack

- Python 3.8+
- Playwright (Sync API)
- Chromium (bundled with Playwright)
- loguru

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/LSL1610/API.git
cd API
```

## Environment Setup

### 1. Create virtual environment
```bash
uv venv
```

### 2. Activate virtual environment
```bash
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
uv sync
uv lock

### 4. Run Command to generate html report
pytest \tests --html=report_api.html
