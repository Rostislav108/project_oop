"""Тесты класса Product и его наследников."""

import pytest

from src.products import BaseProduct, LawnGrass, Product, Smartphone


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


def test_product_str() -> None:
    """Строковое представление товара."""
    product = Product("Samsung", "256GB", 80.0, 15)

    assert str(product) == "Samsung, 80.0 руб. Остаток: 15 шт."


def test_product_add() -> None:
    """Сложение возвращает полную стоимость товаров на складе."""
    first = Product("Товар a", "Описание", 100.0, 10)
    second = Product("Товар b", "Описание", 200.0, 2)

    assert first + second == 1400


def test_smartphone_init() -> None:
    """Проверяет корректность инициализации смартфона."""
    smartphone = Smartphone("Samsung", "Флагман", 80000.0, 5, 3.2, "S23", 256, "серый")

    assert isinstance(smartphone, Product)
    assert smartphone.name == "Samsung"
    assert smartphone.efficiency == 3.2
    assert smartphone.model == "S23"
    assert smartphone.memory == 256
    assert smartphone.color == "серый"


def test_lawn_grass_init() -> None:
    """Проверяет корректность инициализации газонной травы."""
    grass = LawnGrass("Газон", "Семена", 4500.0, 20, "Россия", "10 дней", "зелёный")

    assert isinstance(grass, Product)
    assert grass.name == "Газон"
    assert grass.country == "Россия"
    assert grass.germination_period == "10 дней"
    assert grass.color == "зелёный"


def test_add_same_classes() -> None:
    """Складываются товары одного класса."""
    first = Smartphone("Samsung", "Флагман", 100.0, 10, 3.2, "S23", 256, "серый")
    second = Smartphone("Apple", "Флагман", 200.0, 2, 3.5, "15", 128, "чёрный")

    assert first + second == 1400


def test_add_different_classes_raises() -> None:
    """При сложении товаров разных классов выбрасывается TypeError."""
    smartphone = Smartphone("Samsung", "Флагман", 100.0, 10, 3.2, "S23", 256, "серый")
    grass = LawnGrass("Газон", "Семена", 200.0, 2, "Россия", "10 дней", "зелёный")

    with pytest.raises(TypeError):
        smartphone + grass


def test_smartphone_is_subclass_of_product() -> None:
    """Классы-наследники действительно наследуются от Product."""
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)


def test_base_product_is_abstract() -> None:
    """Абстрактный класс BaseProduct нельзя создать напрямую."""
    with pytest.raises(TypeError):
        BaseProduct("Товар", "Описание", 100.0, 1)


def test_product_is_subclass_of_base() -> None:
    """Продукт и его наследники наследуются от BaseProduct."""
    assert issubclass(Product, BaseProduct)
    assert issubclass(Smartphone, BaseProduct)
    assert issubclass(LawnGrass, BaseProduct)


def test_mixin_prints_on_create(capsys) -> None:
    """Миксин печатает класс и параметры созданного объекта."""
    Product("Продукт1", "Описание продукта", 1200, 10)

    captured = capsys.readouterr()

    assert "Product('Продукт1', 'Описание продукта', 1200, 10)" in captured.out
