import pytest
from playwright.sync_api import sync_playwright
from utils.config import DEFAULT_TIMEOUT_MS


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(
        viewport={"width": 1366, "height": 768},
        user_agent=(
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        ),
    )
    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    yield page
    context.close()
