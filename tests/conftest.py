import pytest
import allure
import json
from pages.login_page import LoginPage


@pytest.fixture(scope="session", autouse=True)
def set_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture(scope="session")
def credentials():
    with open("data/credentials.json", "r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.open()
    return lp

@pytest.fixture
def authenticated_page(request, login_page, credentials):
    user_type = getattr(request, "param", "standard_user")

    user = credentials[user_type]

    login_page.login_to_application(
        user["user_name"],
        user["password"],
    )

    return login_page.page
