import json

import pytest

import config
from exceptions import ScrapingException
from scraper import get_satellite_info

URL = config.SATELLITE_URL


@pytest.mark.usefixtures("mocked_responses")
def test_get_satellite_info_success(mocked_responses):
    altitude = 123.456
    last_updated = "2023-08-23T18:14:50"
    expected_response = {"altitude": altitude, "last_updated": last_updated}
    status_code = 200
    mocked_responses.get(
        URL,
        body=json.dumps(expected_response),
        status=status_code,
        content_type="application/json",
    )

    satellite_info = get_satellite_info()

    assert satellite_info == expected_response

@pytest.mark.parametrize(
    "status_code",
    [
        100, 101, 102, 103,
        201, 202, 203, 204, 205, 206, 207, 208, 226,
        300, 301, 302, 303, 304, 305, 306, 307, 308,
        400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 416, 417, 418, 421, 422, 423, 424,
        425, 426, 428, 429, 431, 451,
        500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511

    ]
)
@pytest.mark.usefixtures("mocked_responses")
def test_get_satellite_info_failures(mocked_responses, status_code):
    mocked_responses.get(
        URL,
        body="",
        status=status_code,
        content_type="application/json",
    )

    with pytest.raises(ScrapingException) as exec:
        get_satellite_info()
