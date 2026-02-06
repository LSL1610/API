from playwright.sync_api import sync_playwright, Response
import json
from loguru import logger
from pathlib import Path
from data import USDExchangeRate

REPORT_DIR = Path("report")


def ensure_report_dir() -> Path:
    """
    Tạo thư mục report nếu chưa tồn tại
    """
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    return REPORT_DIR

def is_target_api(response: Response) -> bool:
    """Chỉ bắt API Exchange của BIDV"""
    try:
        return (
            USDExchangeRate.TARGET_API_KEYWORD in response.url
            and response.request.resource_type in {"xhr", "fetch"}
            and "application/json" in response.headers.get("content-type", "")
        )
    except KeyError:
        return False


def handle_response(response: Response):
    """
    Handle response.
    """
    if not is_target_api(response):
        return

    try:
        with open(ensure_report_dir() / "report_exchange_rate.txt", "w", encoding="utf-8") as f:
            data = response.json()

            logger.info("=== BIDV EXCHANGE API FOUND ===")
            logger.info(f"URL: {response.url}")
            logger.info(f"STATUS: {response.status}")

            logger.debug(
                json.dumps(data, indent=2, ensure_ascii=False)[:500]
            )

            currency = data["data"][0]
            logger.info(f"TIME: {data.get('hour')}")
            f.write(f"TIME: {data.get('hour')}\n")
            logger.info(f"Đồng tiền: {currency.get('currency')}")
            f.write(f"Đồng tiền: {currency.get('currency')}\n")
            logger.info(f"Giá mua tiền mặt: {currency.get('muaTm')}")
            f.write(f"Giá mua tiền mặt: {currency.get('muaTm')}\n")

    except Exception as e:
        logger.error(f"Parse API failed: {e}")


def main():
    """
    Main function.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.on("response", handle_response)

        try:
            page.goto(USDExchangeRate.TARGET_URL, timeout=60_000)
            page.wait_for_timeout(8_000)  # đủ để JS gọi API
        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    main()
