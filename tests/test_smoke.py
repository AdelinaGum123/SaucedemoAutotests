import pytest
import allure
from pages.inventory_page import InventoryPage


@allure.feature("Главная страница")
@allure.title("В заголовке вкладки есть название сайта")
def test_saucedemo_title(login_page):
    login_page.should_have_title("Swag Labs")


@allure.feature("Авторизация")
@allure.story("Успешная авторизация")
@allure.title("Пользователь успешно авторизуется")
def test_successful_login(login_page, credentials):

    login_page.login_to_application(
        credentials["standard_user"]["user_name"],
        credentials["standard_user"]["password"],
    )

    inventory_page = InventoryPage(login_page.page)

    with allure.step("Проверяем переход на страницу каталога товаров"):
        inventory_page.should_have_url()
        inventory_page.should_have_products_title("Products")


@pytest.mark.parametrize(
    "user_name, password, expected_error",
    [
        pytest.param(
            "invalid_user",
            "wrong_password",
            "Epic sadface: Username and password do not match any user in this service",
            id="invalid_credentials",
        ),
        pytest.param(
            "",
            "",
            "Epic sadface: Username is required",
            id="empty_credentials",
        ),
        pytest.param(
            "invalid_user",
            "",
            "Epic sadface: Password is required",
            id="empty_password"
        ),
        pytest.param(
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
            id="locked_out_user"
        )
    ]
)
@allure.feature("Авторизация")
@allure.story("Негативные сценарии")
@allure.title("Проверка ошибок при авторизации")
def test_invalid_credentials(login_page, user_name, password,expected_error):

    login_page.login_to_application(user_name, password)

    with allure.step('Проверяем сообщение об ошибке'):
        login_page.should_have_error_message(
            expected_error
        )

