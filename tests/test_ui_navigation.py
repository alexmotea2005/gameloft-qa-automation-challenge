import pytest
from playwright.sync_api import expect

from utils.config import BASE_URL


@pytest.mark.ui
def test_view_all_links_are_visible_for_game_sections(page):
    page.goto(BASE_URL, wait_until="domcontentloaded")

    view_all_count = page.get_by_text("View all", exact=True).count()
    assert view_all_count >= 3, "Expected several 'View all' links for game sections"


@pytest.mark.ui
def test_mobile_viewport_still_shows_main_brand_and_content(browser):
    context = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True)
    page = context.new_page()
    page.goto(BASE_URL, wait_until="domcontentloaded")

    expect(page.locator("body")).to_contain_text("LUDIGAMES", timeout=15000)
    expect(page.locator("body")).to_contain_text("Play", timeout=15000)

    context.close()
