import requests
from loguru import logger
from pages import Data, DOMAIN1

def login():
    try:
        req = requests.post(url=DOMAIN1,
                            cookies=Data.cookies,
                            headers=Data.headers,
                            data=Data.data)
        logger.debug(f"Response: {req.status_code}")
        
    except TimeoutError as te:
        logger.error(f"Timeout: {te}")
        
    except Exception as e:
        logger.error(f"Error: {e}")
    