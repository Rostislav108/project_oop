"""Тесты класса Category."""

import pytest

from src.categories import Category, CategoryIterator
from src.products import Product, Smartphone


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


def test_products_getter_returns_string(products: list[Product]) -> None:
    """Геттер возвращает строку со всеми товарами по шаблону."""
    category = Category("Смартфоны", "Описание", products)

    expected = (
        "Samsung, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert category.products == expected


def test_products_attribute_is_private(products: list[Product]) -> None:
    """Список товаров хранится в приватном атрибуте."""
    category = Category("Смартфоны", "Описание", products)

    assert isinstance(category._Category__products, list)
    assert not hasattr(category, "__products")


def test_add_product(products: list[Product]) -> None:
    """Метод add_product добавляет товар и увеличивает счётчик."""
    category = Category("Смартфоны", "Описание", products)

    category.add_product(Product("Xiaomi", "128GB", 31000.0, 14))

    assert "Xiaomi" in category.products
    assert Category.product_count == 3


def test_add_product_returns_none(products: list[Product]) -> None:
    """Метод add_product не возвращает значения."""
    category = Category("Смартфоны", "Описание", products)

    assert category.add_product(Product("Xiaomi", "128GB", 31000.0, 14)) is None


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


def test_category_str(products: list[Product]) -> None:
    """Строковое представление категории по общему числу товаров."""
    category = Category("Смартфоны", "Описание", products)

    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_category_iterator(products: list[Product]) -> None:
    """Перебирает товары категории в цикле for."""
    category = Category("Смартфоны", "Описание", products)

    names = [product.name for product in CategoryIterator(category)]

    assert names == ["Samsung", "Iphone"]


def test_add_product_accepts_subclass() -> None:
    """Метод add_product принимает наследников класса Product."""
    category = Category("Смартфоны", "Описание", [])
    smartphone = Smartphone("Samsung", "Флагман", 80000.0, 5, 3.2, "S23", 256, "серый")

    category.add_product(smartphone)

    assert "Samsung" in category.products
    assert Category.product_count == 1


def test_add_product_rejects_non_product() -> None:
    """Метод add_product отклоняет объекты, не являющиеся товаром."""
    category = Category("Смартфоны", "Описание", [])

    with pytest.raises(TypeError):
        category.add_product("это не товар")
