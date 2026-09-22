"""Тесты класса Category."""

import pytest

from src.categories import Category
from src.products import Product


@pytest.fixture(autouse=True)
def reset_counters() -> None:
    """Сбрасывает атрибуты класса перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def products() -> list[Product]:
    """Возвращает список товаров для тестов."""
    return [
        Product("Samsung", "256GB", 180000.0, 5),
        Product("Iphone", "512GB", 210000.0, 8),
    ]


def test_category_init(products: list[Product]) -> None:
    """Проверяет корректность инициализации категории."""
    category = Category("Смартфоны", "Описание", products)

    assert category.name == "Смартфоны"
    assert category.description == "Описание"
    assert category.products == products
    assert len(category.products) == 2


def test_category_count(products: list[Product]) -> None:
    """Проверяет подсчёт количества категорий."""
    Category("Смартфоны", "Описание", products)
    Category("Телевизоры", "Описание", [])

    assert Category.category_count == 2


def test_product_count(products: list[Product]) -> None:
    """Проверяет подсчёт количества товаров."""
    Category("Смартфоны", "Описание", products)
    assert Category.product_count == 2

    Category("Телевизоры", "Описание", [Product("ТВ", "4K", 1000.0, 1)])
    assert Category.product_count == 3


def test_counters_accessible_from_object(products: list[Product]) -> None:
    """Атрибуты класса доступны через объект."""
    category = Category("Смартфоны", "Описание", products)

    assert category.category_count == 1
    assert category.product_count == 2
