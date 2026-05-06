import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


BASE_URL = "https://adnabu-store-assignment1.myshopify.com"
STORE_PASSWORD = "AdNabuQA"
SEARCH_KEYWORD = "snowboard"
TIMEOUT = 15


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def enter_store_password(driver, wait, password):
    driver.get(BASE_URL)
    password_input = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    wait.until(EC.url_contains("/"))


def open_search_and_type(driver, wait, keyword):
    search_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "summary.header__icon--search"))
    )
    search_icon.click()
    search_input = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='q']"))
    )
    search_input.send_keys(keyword)


def click_product_from_dropdown(driver, wait):
    product = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='The Complete Snowboard']"))
    )
    product.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))


def add_to_cart(driver, wait):
    btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='add']"))
    )
    btn.click()


def get_cart_count(driver, wait):
    count = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-count-bubble span"))
    )
    return count.text.strip()


def test_search_and_add_to_cart(driver):
    wait = WebDriverWait(driver, TIMEOUT)

    enter_store_password(driver, wait, STORE_PASSWORD)
    open_search_and_type(driver, wait, SEARCH_KEYWORD)
    click_product_from_dropdown(driver, wait)

    add_to_cart(driver, wait)

    cart_count = get_cart_count(driver, wait)
    assert cart_count == "1", f"Expected cart count 1, got '{cart_count}'"