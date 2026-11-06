import allure

from pages.base_page import BasePage
from playwright.sync_api import Locator, Page, expect


class InventoryPage(BasePage):
    PATH = "/inventory.html"

    def __init__(self, page: Page):
        super().__init__(page)

        self.burger_menu: Locator = page.locator("#react-burger-menu-btn")
        self.cart: Locator = page.locator("[data-test='shopping-cart-link']")
        self.filter: Locator = page.locator("[data-test='product-sort-container']")
        self.logo: Locator = page.locator(".app_logo")
        self.page_title: Locator = page.locator("[data-test='title']")
        self.cart_badge: Locator = page.locator("[data-test='shopping-cart-badge']")

    def add_product_to_cart(self, product_name: str) -> None:
        locator = self.page.locator(
        f"[data-test='add-to-cart-sauce-labs-{product_name}']")
        self.click(locator)

    def open_cart(self) -> None:
        self.click(self.cart)

    def open_burger_menu(self) -> None:
        self.click(self.burger_menu)

    @allure.step("Проверяем заголовок")
    def should_have_products_title(self, expected_title: str) -> None:
        self.should_be_visible(self.page_title, "Заголовок страницы")
        expect(self.page_title).to_have_text(expected_title)

    @allure.step("Проверяем количество товаров в корзине")
    def should_have_cart_badge(self, expected_count: str) -> None:
        expect(self.cart_badge).to_have_text(expected_count)

    @allure.title("Проверяем что корзина пуста")
    def should_dont_have_cart_badge(self) -> None:
        self.should_not_be_visible(self.cart_badge)


    @allure.title("Удаление товара из корзины")
    def remove_product_from_cart(self, product_name: str) -> None:
        locator = self.page.locator(
        f"[data-test='remove-sauce-labs-{product_name}']")
        self.click(locator)



