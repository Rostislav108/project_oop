"""Тесты класса Product."""

from src.products import Product


def test_product_init() -> None:
    """Проверяет корректность инициализации товара."""
    product = Product("Samsung", "256GB", 180000.0, 5)

    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_getter() -> None:
    """Геттер возвращает значение приватной цены."""
    product = Product("Samsung", "256GB", 199.99, 5)

    assert product.price == 199.99
    assert isinstance(product.price, float)


def test_price_setter_updates_price() -> None:
    """Сеттер обновляет цену при положительном значении."""
    product = Product("Samsung", "256GB", 180000.0, 5)

    product.price = 170000.0

    assert product.price == 170000.0


def test_price_setter_rejects_zero(capsys) -> None:
    """Сеттер не принимает нулевую цену и выводит сообщение."""
    product = Product("Samsung", "256GB", 180000.0, 5)

    product.price = 0

    assert product.price == 180000.0
    assert "Цена не должна быть нулевая или отрицательная" in capsys.readouterr().out


def test_price_setter_rejects_negative(capsys) -> None:
    """Сеттер не принимает отрицательную цену и выводит сообщение."""
    product = Product("Samsung", "256GB", 180000.0, 5)

    product.price = -100

    assert product.price == 180000.0
    assert "Цена не должна быть нулевая или отрицательная" in capsys.readouterr().out


def test_new_product() -> None:
    """Класс-метод создаёт товар из словаря с параметрами."""
    data = {"name": "Iphone", "description": "512GB", "price": 210000.0, "quantity": 8}

    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Iphone"
    assert product.description == "512GB"
    assert product.price == 210000.0
    assert product.quantity == 8
