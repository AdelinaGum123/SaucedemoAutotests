import pytest
import allure
import json
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def open_home_page(page, base_url):
    page.goto(base_url)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Этот хук проверяет статус выполнения теста
    outcome = yield
    rep = outcome.get_result()

    # Проверяем, что тест завершился с ошибкой на этапе вызова (call)
    if rep.when == "call" and rep.failed:
        # Пытаемся достать фикстуру 'page' из упавшего теста
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            # Делаем скриншот в виде байтов
            screenshot = page.screenshot(full_page=True)
            # Прикрепляем скриншот к отчету Allure
            allure.attach(
                screenshot,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.fixture(scope="session")
def credentials():
    """Читает учетные данные из JSON один раз на всю сессию"""
    with open("data/credentials.json", "r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture
def login_page(page, base_url):
    """Создает объект LoginPage и сразу открывает сайт"""
    lp = LoginPage(page)
    lp.open_url(base_url)
    return lp
