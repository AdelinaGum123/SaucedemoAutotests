# Файл хранит общие методы, которые нужны на любой странице
from playwright.sync_api import Locator, Page, expect
import allure
import re


class BasePage:
    # Путь страницы относительно base_url
    PATH = '/'

    def __init__(self, page: Page):
        # Сохраняем вкладку браузера внутри класса, чтобы управлять ей в других методах
        self.page = page

    @allure.step("Открываем страницу")
    def open(self) -> None:
        with allure.step(f"Переходим по адресу {self.PATH}"):
            self.page.goto(self.PATH)

    @allure.step("Проверяем заголовок вкладки")
    def should_have_title(self, title: str) -> None:
        expect(self.page).to_have_title(title)

    @allure.step("Проверяем, что открыта страница")
    def should_have_url(self) -> None:
        expect(self.page).to_have_url(
            re.compile(f".*{re.escape(self.PATH)}$")
        )

    @allure.step("Клик по элементу")
    def click(self, locator: Locator) -> None:
        locator.click()

    @allure.step("Ввод текста в поле")
    def fill(self, locator: Locator, text: str, name: str) -> None:
        locator.fill(text)

    @allure.step("Проверка, что текущий URL содержит")
    def verify_url_contains(self, expected_substring: str) -> None:
        expect(self.page).to_have_url(
            re.compile(f".*{re.escape(expected_substring)}.*")
        )

    @allure.step("Проверяем видимость элемента")
    def should_be_visible(self, locator: Locator, name: str) -> None:
        with allure.step(f"Элемент «{name}» виден на странице"):
            expect(locator).to_be_visible()

    @allure.step("Получаем текст элемента")
    def get_text(self, locator: Locator) -> str:
        return locator.inner_text()

    @allure.step("Проверяем отсутствие элемента")
    def should_not_be_visible(self, locator: Locator, name: str) -> None:
        with allure.step(f"Элемент «{name}» не виден на странице"):
            expect(locator).not_to_be_visible()
