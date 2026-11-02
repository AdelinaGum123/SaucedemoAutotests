import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import allure



@allure.feature("Главная страница")
@allure.title("В заголовке вкладки есть название сайта")
def test_saucedemo_title(login_page):
    login_page.should_have_title("Swag Labs")


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
        credentials["invalid_user"]["user_name"],
        credentials["invalid_user"]["password"],
    )

    with allure.step('Проверяем сообщение об ошибке'):
        login_page.should_have_error_message(
            "Epic sadface: Username and password do not match any user in this service"
        )


@pytest.mark.parametrize(
    "user_name, password, expected_error",
    [
        (
        "invalid_user",
         "wrong_password",
        "Epic sadface: Username and password do not match any user in this service",
        ),
        (
        "",
        "",
        "Epic sadface: Username is required",
        ),
        ("invalid_user",
         "",
        "Epic sadface: Password is required",
        ),
        ("locked_out_user",
         "secret_sauce",
         "Epic sadface: Sorry, this user has been locked out.",
        )
    ]
)
def test_invalid_credentials(page, user_name, password,expected_error):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login_to_application(user_name, password)

    with allure.step('Проверяем сообщение об ошибке'):
        login_page.should_have_error_message(
            expected_error
        )

