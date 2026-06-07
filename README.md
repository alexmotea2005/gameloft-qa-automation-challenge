# Gameloft QA Automation & AI Internship Challenge

Automation suite for `https://play.ludigames.com`, created for the Gameloft Builders Lab QA Automation & AI Internship application challenge.

The suite mixes UI browser tests and API/HTTP checks. The goal is to validate important user flows and basic availability risks on the Ludigames portal.

## Tech stack

- Python 3.10+
- pytest
- Playwright
- requests
- pytest-html

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

## Run the tests

```bash
pytest
```

Run only UI tests:

```bash
pytest -m ui
```

Run only API tests:

```bash
pytest -m api
```

An HTML report is generated at:

```text
reports/report.html
```

## Automated scenarios

### 1. Homepage availability and response time - API

The test sends an HTTP GET request to the Ludigames homepage and checks that the response is `200`, contains Ludigames branding, and responds under an acceptable threshold.

Why: if the homepage is down or very slow, the whole user journey is affected immediately.

### 2. Homepage contains important game sections - API

The test checks that important sections such as `Sport`, `Action`, and `Racing` are present in the homepage HTML.

Why: these sections are core navigation elements for users browsing games by category.

### 3. Static assets are not broken - API

The test extracts a small sample of same-origin JavaScript/CSS assets from the homepage and verifies that they do not return an error status.

Why: broken frontend assets can make the page unusable even when the HTML itself returns `200`.

### 4. Homepage loads and shows main content - UI

The browser opens the homepage and verifies that the brand and basic playable content are visible.

Why: this validates the actual user-facing page, not only the raw HTTP response.

### 5. Core categories are visible - UI

The browser verifies that category labels like `Sport`, `Action`, and `Racing` are visible.

Why: users expect category navigation to work when discovering games.

### 6. Game entries are visible - UI

The browser checks that recognizable game entries or play buttons are visible.

Why: the main purpose of the portal is to let users find and start games.

### 7. Legal footer links are visible - UI

The browser verifies that privacy, terms, and cookie policy links are available.

Why: these links are important for compliance and user trust.

### 8. Mobile viewport smoke test - UI

The browser opens the homepage using a mobile viewport and verifies that the main content is still present.

Why: many users access browser games from mobile devices, so a basic mobile smoke test is valuable.

## Example terminal output

Paste your real output here after running `pytest`, for example:

```text
9 passed in 9.07s
## Notes

The tests intentionally use stable text-based checks instead of fragile CSS selectors. This makes the suite easier to understand and less likely to fail because of small layout changes.
