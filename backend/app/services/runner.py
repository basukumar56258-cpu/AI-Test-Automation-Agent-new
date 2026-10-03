from playwright.sync_api import sync_playwright

def run_smoke_test(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            response = page.goto(url, wait_until="domcontentloaded", timeout=30000)
            return {"status":"passed", "url":page.url, "http_status": response.status if response else None, "title":page.title()}
        except Exception as exc:
            return {"status":"failed", "error":str(exc)}
        finally:
            browser.close()
