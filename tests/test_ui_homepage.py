import pytest
from playwright.sync_api import expect

from utils.config import BASE_URL


@pytest.mark.ui
def test_homepage_loads_and_displays_content(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")

    expect(page).to_have_url(BASE_URL + "/")
    expect(page.locator("body")).to_be_visible()

    body_text = page.locator("body").inner_text(timeout=15000)
    assert len(body_text.strip()) > 0


@pytest.mark.ui
def test_homepage_contains_game_related_content(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")

    body_text = page.locator("body").inner_text(timeout=15000).lower()

    expected_keywords = ["game", "play", "sport", "action", "racing"]
    assert any(keyword in body_text for keyword in expected_keywords)


@pytest.mark.ui
def test_homepage_has_clickable_links(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")

    links = page.locator("a[href]")
    assert links.count() > 0

    first_href = links.first.get_attribute("href")
    assert first_href is not None
    assert first_href.strip() != ""


@pytest.mark.ui
def test_footer_or_legal_content_exists_in_dom(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")

    html = page.content().lower()

    assert "privacy" in html or "terms" in html or "legal" in html
