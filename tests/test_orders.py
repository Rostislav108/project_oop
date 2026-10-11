"""Тесты класса Order."""

from src.base import BaseNamedEntity
from src.orders import Order
from src.products import Product


def test_order_init_and_total_cost() -> None:
    """Проверяет создание заказа и расчёт итоговой стоимости."""
    product = Product("Товар", "Описание", 100.0, 10)

    order = Order("Заказ №1", product, 3)

    assert isinstance(order, BaseNamedEntity)
    assert order.name == "Заказ №1"
    assert order.product is product
    assert order.quantity == 3
    assert order.total_cost == 300.0


def test_order_holds_single_product() -> None:
    """В заказе указывается только один товар."""
    product = Product("Товар", "Описание", 50.0, 100)

    order = Order("Заказ №2", product, 4)

    assert order.total_cost == 200.0
