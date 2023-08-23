from typing import Dict

import requests

import config
from exceptions import ScrapingException

URL = config.SATELLITE_URL


def get_satellite_info() -> Dict:
    try:
        response = requests.get(URL)
    except Exception:
        raise ScrapingException(f"{URL} didn't return successful response.")

    if response.status_code == 200:
        json_response = response.json()
        return {
            "altitude": json_response["altitude"],
            "last_updated": json_response["last_updated"]
        }
    else:
        raise ScrapingException(f"{URL} didn't return successful response. Status code {response.status_code}")
