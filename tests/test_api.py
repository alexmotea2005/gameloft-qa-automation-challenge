import re
import time
from urllib.parse import urljoin, urlparse

import pytest
import requests

from utils.config import BASE_URL


@pytest.mark.api
def test_homepage_returns_success_status_code():
    response = requests.get(BASE_URL, timeout=10)

    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "").lower()


@pytest.mark.api
def test_homepage_response_time_is_acceptable():
    start = time.perf_counter()
    response = requests.get(BASE_URL, timeout=10)
    elapsed = time.perf_counter() - start

    assert response.status_code == 200
    assert elapsed < 5


@pytest.mark.api
def test_homepage_contains_links_to_browsable_resources():
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()

    links = re.findall(r'href=["\']([^"\']+)["\']', response.text)
    browsable_links = [
        urljoin(BASE_URL, link)
        for link in links
        if link and not link.startswith(("mailto:", "tel:", "javascript:", "#"))
    ]

    assert browsable_links, "Homepage should expose at least one browsable link"

    # Validate only a few links to keep the test fast and stable.
    for link in browsable_links[:5]:
        parsed = urlparse(link)
        assert parsed.scheme in ["http", "https"]

        check = requests.get(link, timeout=10, allow_redirects=True)
        assert check.status_code < 500
