"""Модуль с классом Product."""


class Product:
    """Товар интернет-магазина.

    Attributes:
        name: название товара.
        description: описание товара.
        price: цена товара (может быть с копейками).
        quantity: количество товара в наличии (в штуках).
    """

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        """Инициализирует товар.

        Args:
            name: название товара.
            description: описание товара.
            price: цена товара.
            quantity: количество товара в наличии.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
