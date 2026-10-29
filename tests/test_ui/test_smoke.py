from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import Page, expect
import allure



@allure.title('В заголовке вкладки имеется нужное слово')
def test_saucedemo_title(page):
    assert "Swag Labs" in page.title()


@allure.title('Успешная авторизация')
def test_successful_login(page, base_url, credentials):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login_to_application(
        credentials["standard_user"]["user_name"],
        credentials["standard_user"]["password"],
    )

    with allure.step('Проверяем, что после логина нас перебросило на страницу каталога товаров'):
        assert page.url == f'{base_url}{InventoryPage.PAGE_URL}'


@allure.title('Вывод ошибки при неправильном логине и пароле')
def test_invalid_login(page, credentials):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login_to_application(
        credentials["standard_user"]["user_name"],
        credentials["standard_user"]["password"],
    )

    with allure.step('Проверяем сообщение об ошибке'):
        login_page.should_have_error_message(
            "Epic sadface: Username and password do not match any user in this service"
        )
