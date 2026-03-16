from playwright.sync_api import sync_playwright
from loguru import logger
from pathlib import Path
from data import GoldPrice

REPORT_DIR = Path("report")

def ensure_report_dir() -> Path:
    """Create report directory if it does not exist."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    return REPORT_DIR


def fetch_gold_price(context) -> dict:
    """Fetch gold price data from SJC API."""
    response = context.request.post(
        GoldPrice.SJC_PRICE_API,
        headers=GoldPrice.headers,
        timeout=10_000
    )
    response.raise_for_status()
    return response.json()


def parse_gold_price(data_json: dict) -> dict:
    """Parse gold price information."""
    gold = data_json["data"][0]
    return {
        "type": gold["TypeName"],
        "buy": gold["Buy"],
        "sell": gold["Sell"],
    }


def save_report(report_path: Path, gold_data: dict) -> None:
    """Save gold price report to file."""
    with report_path.open("w", encoding="utf-8") as f:
        f.write(
            f"Type Gold : {gold_data['type']}\n"
            f"Buy Price : {gold_data['buy']}\n"
            f"Sell Price: {gold_data['sell']}\n"
        )

def main():
    """
    Main function.
    """
    report_path = ensure_report_dir() / GoldPrice.REPORT_FILE

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        try:
            data_json = fetch_gold_price(context)
            gold_data = parse_gold_price(data_json)
            save_report(report_path, gold_data)

            logger.info("Gold price report generated successfully")

        except Exception as e:
            logger.error(f"Failed to get gold price: {e}")

        finally:
            browser.close()


if __name__ == "__main__":
    main()
