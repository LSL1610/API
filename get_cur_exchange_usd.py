from playwright.sync_api import sync_playwright
import json
import requests
from loguru import logger

TARGET_URL = "https://bidv.com.vn/en/ca-nhan/cong-cu-tien-ich/ty-gia-ngoai-te-gia-vang"
API_EXCHANGE = "https://bidv.com.vn/ServicesBIDV/ExchangeRateServlet"


def is_api_response(response):
    """Chỉ lọc XHR / Fetch và content-type json"""
    try:
        return (
            response.request.resource_type in ["xhr", "fetch"]
            and "application/json" in response.headers.get("content-type", "")
        )
    except Exception:
        return False


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        api_responses = []

        def handle_response(response):
            if is_api_response(response):
                try:
                    data = response.json()
                    api_responses.append({
                        "url": response.url,
                        "status": response.status,
                        "data": data
                    })

                    logger.warning("\n=== API FOUND ===")
                    logger.debug(response.url)
                    if "ExchangeDetailServlet" in str(response.url):
                        logger.warning(f"URL: {response.url}")
                        logger.warning(f"STATUS: {response.status}")
                        data_json = json.dumps(data, indent=2)[:000]
                        logger.debug(type(data_json))
                        logger.debug(data_json)
                        data_json = json.loads(data_json)
                        logger.warning(f"TIME: {data_json["hour"]}")
                        logger.warning(f"Đồng tiền: {data_json["data"][0]["currency"]}")
                        logger.warning(f"Giá Mua Tiền Mặt: {data_json["data"][0]["muaTm"]}")
                        return
                    
                except Exception:
                    pass

        page.on("response", handle_response)

        page.goto(TARGET_URL, timeout=60000)
        page.wait_for_timeout(10000)  # đợi JS load xong

        browser.close()

if __name__ == "__main__":
    main()
