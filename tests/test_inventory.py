import pytest
from pages.inventory_page import InventoryPage
import allure

@allure.title('Проверка открытия страницы товаров и заголовка')
def test_have_title(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)

    inventory_page.should_have_url()
    inventory_page.should_have_products_title("Products")

@pytest.mark.parametrize(
    ("products", "expected_count"),
    [
        pytest.param(["backpack"], "1", id="one-product"),
        pytest.param(["backpack", "bike-light"], "2", id="two-products")
    ],
)
@allure.title('Проверка добавления товаров в корзину')
def test_add_product_to_cart(products, expected_count, authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    for product in products:
        inventory_page.add_product_to_cart(product)
    inventory_page.should_have_cart_badge(expected_count)

@allure.title('Проверка удаления товара из корзины')
def test_remove_product_from_cart(page, authenticated_page):
    inventory_page = InventoryPage(authenticated_page)

    inventory_page.add_product_to_cart('backpack')
    inventory_page.should_have_cart_badge('1')
    inventory_page.remove_product_from_cart('backpack')
    inventory_page.should_dont_have_cart_badge()

