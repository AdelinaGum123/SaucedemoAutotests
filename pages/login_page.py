import allure
from pages.base_page import BasePage
from playwright.sync_api import Locator, Page, expect


class LoginPage(BasePage):
    PATH = '/'

    def __init__(self, page: Page):
        super().__init__(page)

        self.user_name: Locator = page.get_by_test_id("username")
        self.password: Locator = page.get_by_test_id("password")
        self.login_button: Locator = page.get_by_test_id("login-button")
        self.error_message: Locator = page.get_by_test_id("error")

    @allure.step("Авторизация в личном кабинете")
    def login_to_application(self, user_name: str, password: str) -> None:
        self.fill(self.user_name, user_name, "Логин")
        self.fill(self.password, password, "Пароль")
        self.click(self.login_button)

    @allure.step("Проверяем сообщение об ошибке авторизации")
    def should_have_error_message(self, expected_text: str) -> None:
        self.should_be_visible(self.error_message, "Сообщение об ошибке")
        expect(self.error_message).to_have_text(expected_text)

