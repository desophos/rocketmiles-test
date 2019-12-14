import pytest
from pytest_bdd import given, parsers, scenario, then, when
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def try_wait_until(driver, condition, error_msg):
    try:
        return WebDriverWait(driver, 5).until(condition)
    except TimeoutException as e:
        raise TimeoutException(error_msg, e.screen, e.stacktrace)


@pytest.fixture(scope="module")
def driver(request):
    options = Options()
    options.headless = True
    with webdriver.Firefox(options=options) as driver:
        yield driver


@scenario("search.feature", "Default search parameters")
def test_search():
    pass


@given(parsers.parse("I am at {base_url}"))
def start_page(driver, base_url):
    driver.get(base_url)
    return base_url


@when("I click the search button")
def search(driver):
    try_wait_until(
        driver,
        EC.element_to_be_clickable((By.CLASS_NAME, "search-submit-btn")),
        "search couldn't find search button",
    ).click()


@then("the search should not be performed")
def is_same_page(driver, start_page):
    assert driver.current_url == start_page


@then(parsers.parse('the "{error_text}" error should appear'))
def wait_for_error(driver, error_text):
    try_wait_until(
        driver,
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "popover-content"), error_text
        ),
        "wait_for_error timed out looking for '{0}'".format(error_text),
    )
