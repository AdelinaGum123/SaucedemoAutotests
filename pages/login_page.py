from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    USER_NAME = "input#user-name"
    PASSWORD = "input#password"
    LOGIN_BUTTON = "input#login-button"
    ERROR_BUTTON = "button.error-button"

    @allure.step("Авторизация с логином: {user_name} и паролем: {password}")
    def login_to_application(self, user_name: str, password: str):
        self.fill_element(LoginPage.USER_NAME, user_name)
        self.fill_element(LoginPage.PASSWORD, password)
        self.click_element(LoginPage.LOGIN_BUTTON)

    @allure.step("Кнопка ошибки есть на странице")
    def visible_error_button(self) -> bool:
        return self.is_element_visible(LoginPage.ERROR_BUTTON)



