import pytest
from playwright.sync_api import sync_playwright, expect

def test_shirt_purchase():
    with sync_playwright() as p:
        
        #----Setting up browser----#
        browser =  p.chromium.launch(headless=False)
        context =  browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page =  context.new_page()
        page.goto("https://automationteststore.com/")
        
        #----Creating a new profile----#
        page.get_by_role("link", name="Account").click()
        page.get_by_role("button", name="Continue").click()

        page.locator("#AccountFrm_firstname").fill("Test")
        page.locator("#AccountFrm_lastname").fill("Name")
        page.locator("#AccountFrm_email").fill("test.name0208@gmail.com")
        page.locator("#AccountFrm_telephone").fill("+36201234567")
        page.select_option("select#AccountFrm_country_id", "Hungary")
        page.locator("#AccountFrm_postcode").fill("6722")
        page.select_option("select#AccountFrm_zone_id", "Csongrad")
        page.locator("#AccountFrm_city").fill("Szeged")
        page.locator("#AccountFrm_address_1").fill("Boldogasszony sgrt. 10")

        page.locator("#AccountFrm_loginname").fill("test_name0208")
        page.locator("#AccountFrm_password").fill("1234")
        page.locator("#AccountFrm_confirm").fill("1234")

        page.locator("#AccountFrm_newsletter0").click()
        page.locator("#AccountFrm_agree").click()

        page.get_by_role("button", name="Continue").click()

        #----Ordering shirts by highest price first----#
        page.get_by_role("link", name="Apparel & accessories").click()
        page.locator("#maincontainer").get_by_role("link", name="T-shirts", exact=True).click()
        page.select_option("select#sort", "Price High > Low")

        #----Putting shirts into cart----#
        page.get_by_role("link", name="Designer Men Casual Formal").click()
        page.locator(".cart").click()
        page.get_by_text("Continue Shopping").click()
        page.get_by_role("link", name="T-shirts").click()
        page.select_option("select#sort", "Price High > Low")
        page.get_by_role("link", name="Casual 3/4 Sleeve Baseball T-Shirt").click()
        page.locator(".cart").click()

        #----Buying the shirts----#
        page.locator("#cart_checkout2").click()
        page.locator("#checkout_btn").click()

        #----Checking if the purchase was successful----#
        expect(page).to_have_url("https://automationteststore.com/index.php?rt=checkout/success")

        context.tracing.stop(path="test-results/trace.zip")
        browser.close()
