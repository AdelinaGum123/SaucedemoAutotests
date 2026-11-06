import pytest

from pages import inventory_page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import allure

@allure.title('Проверка открытия страницы товаров и заголовка')
def test_have_title(page, credentials):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login_to_application(
        credentials["standard_user"]["user_name"],
        credentials["standard_user"]["password"],
    )

    inventory_page = InventoryPage(page)

    inventory_page.should_have_url()
    inventory_page.should_have_products_title("Products")

@allure.title('Проверка добавления одного товара в корзину')
def test_add_product_to_cart(page, credentials):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login_to_application(
        credentials["standard_user"]["user_name"],
        credentials["standard_user"]["password"],
    )

    inventory_page = InventoryPage(page)

    inventory_page.add_product_to_cart('backpack')
    inventory_page.should_have_cart_badge('1')

@allure.title('Проверка добавления двух товаров в корзину')
def test_add_product_to_cart(page, credentials):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login_to_application(
        credentials["standard_user"]["user_name"],
        credentials["standard_user"]["password"],
    )

    inventory_page = InventoryPage(page)

    inventory_page.add_product_to_cart('backpack')
    inventory_page.add_product_to_cart('bike-light')
    inventory_page.should_have_cart_badge('2')

@allure.title('Проверка удаления товара из корзины')
def test_remove_product_from_cart(page, credentials):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login_to_application(
        credentials["standard_user"]["user_name"],
        credentials["standard_user"]["password"],
    )

    inventory_page = InventoryPage(page)

    inventory_page.add_product_to_cart('backpack')
    inventory_page.should_have_cart_badge('1')
    inventory_page.remove_product_from_cart('backpack')
    inventory_page.should_dont_have_cart_badge()

