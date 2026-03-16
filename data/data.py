class GoldPrice:
    
    cookies = {
        '_ga': 'GA1.1.695975451.1768878118',
        '_gcl_au': '1.1.1917606139.1768878118',
        'ASP.NET_SessionId': '87abf288-0f1d-4a69-aeb9-d5f5b2fcd646',
        'SRV': '154e77e7-a844-45fd-a837-f87154b48930',
        '_ga_JM090DV136': 'GS2.1.s1770361845$o3$g1$t1770362164$j60$l0$h2134460556',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'origin': 'https://sjc.com.vn',
        'priority': 'u=1, i',
        'referer': 'https://sjc.com.vn/?utm_source=chatgpt.com',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    REPORT_FILE = "report_gold_price.txt"
    SJC_PRICE_API = "https://sjc.com.vn/GoldPrice/Services/PriceService.ashx"


class USDExchangeRate:
    TARGET_URL = "https://bidv.com.vn/en/ca-nhan/cong-cu-tien-ich/ty-gia-ngoai-te-gia-vang"
    TARGET_API_KEYWORD = "ExchangeDetailServlet"
