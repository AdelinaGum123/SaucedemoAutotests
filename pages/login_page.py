from pages.base_page import BasePage
from playwright.sync_api import Locator, Page
import allure


class LoginPage(BasePage):
    PATH = '/'

    USER_NAME = "input#user-name"
    PASSWORD = "input#password"
    LOGIN_BUTTON = "input#login-button"
    ERROR_BUTTON = "button.error-button"
    ERROR_MESSAGE = "h3[data-test='error']"

    def __init__(self, page: Page):
        super().__init__(page)

        self.user_name: Locator = page.locator(self.USER_NAME)
        self.password: Locator = page.locator(self.PASSWORD)
        self.login_button: Locator = page.locator(self.LOGIN_BUTTON)
        self.error_message: Locator = page.locator(self.ERROR_BUTTON)

    @allure.step("Авторизация в личном кабинете")
    def login_to_application(self, user_name: str, password: str):
        self.fill(self.user_name, user_name, "Логин")
        self.fill(self.password, password, "Пароль")
        self.click(self.login_button)

    @allure.step("Проверяем сообщение об ошибке авторизации")
    def should_have_error_message(self, expected_text: str) -> None:
        error_message = self.page.locator(self.ERROR_MESSAGE)

        self.should_be_visible(error_message, "Сообщение об ошибке")

        actual_text = self.get_text(error_message)

        assert actual_text == expected_text, (
            f"Текст ошибки не соответствует ожидаемому. "
            f"Ожидалось: '{expected_text}'. Получено: '{actual_text}'"
        )

