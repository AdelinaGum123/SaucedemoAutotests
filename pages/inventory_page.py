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
    


