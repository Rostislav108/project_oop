"""Модуль с классом Order (заказ)."""

from src.base import BaseNamedEntity
from src.exceptions import ZeroQuantityError
from src.products import Product


class Order(BaseNamedEntity):
    """Заказ на один товар.

    Attributes:
        product: товар, который был куплен.
        quantity: количество купленного товара.
    """

    def __init__(self, name: str, product: Product, quantity: int) -> None:
        """Инициализирует заказ.

        Args:
            name: название заказа.
            product: покупаемый товар.
            quantity: количество товара.

        Raises:
            ZeroQuantityError: если у товара нулевое количество.
        """
        if product.quantity == 0:
            raise ZeroQuantityError(
                "Товар с нулевым количеством не может быть добавлен"
            )
        super().__init__(name)
        self.product = product
        self.quantity = quantity

    @property
    def total_cost(self) -> float:
        """Возвращает итоговую стоимость заказа.

        Returns:
            Произведение цены товара на его количество.
        """
        return self.product.price * self.quantity
