# Файл хранит общие методы, которые нужны на любой странице
from playwright.sync_api import Page, expect
import allure


class BasePage:
    def __init__(self, page: Page):
        # Сохраняем вкладку браузера внутри класса, чтобы управлять ей в других методах
        self.page = page

    @allure.step("Открываем {url} браузере, ждем пока страница загрузится")
    def open_url(self, url: str):
        return self.page.goto(url)

    @allure.step("Возвращает текстовый заголовок текущей вкладки браузера")
    def get_title(self) -> str:
        return self.page.title()


    @allure.step("Клик по элементу с селектором: {selector}")
    def click_element(self, selector: str):
        self.page.locator(selector).click()


    @allure.step("Ввод текста в элемент с селектором: {selector}")
    def fill_element(self, selector: str, text: str):
        self.page.locator(selector).fill(text)


    @allure.step("Проверка, что текущий URL содержит: {expected_substring}")
    def verify_url_contains(self, expected_substring: str):
        expect(self.page).to_have_url(lambda url: expected_substring in url)

    @allure.step("Элемент с селектором: {selector} видим на странице")
    def is_element_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()


