"""Тесты класса Product."""

from src.products import Product


def test_product_init() -> None:
    """Проверяет корректность инициализации товара."""
    product = Product("Samsung", "256GB", 180000.0, 5)

    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_with_kopeks() -> None:
    """Цена товара может быть указана с копейками."""
    product = Product("Товар", "Описание", 199.99, 1)

    assert product.price == 199.99
    assert isinstance(product.price, float)
