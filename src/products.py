"""Модуль с классом Product."""

from typing import Any


class Product:
    """Товар интернет-магазина.

    Attributes:
        name: название товара.
        description: описание товара.
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
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict[str, Any]) -> "Product":
        """Создаёт товар из словаря с его параметрами.

        Args:
            product_data: словарь с ключами name, description,
                price и quantity.

        Returns:
            Новый объект класса Product.
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену, если она положительная.

        Args:
            new_price: новое значение цены.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    def __str__(self) -> str:
        """Возвращает строковое представление товара.

        Returns:
            Строка вида «Название продукта, X руб. Остаток: X шт.».
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает полную стоимость товаров на складе.

        Args:
            other: второй товар для сложения.

        Returns:
            Сумма произведений цены на количество у двух товаров.

        Raises:
            TypeError: если товары относятся к разным классам.
        """
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного класса")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Смартфон — наследник класса Product.

    Attributes:
        efficiency: производительность.
        model: модель.
        memory: объём встроенной памяти.
        color: цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует смартфон.

        Args:
            name: название товара.
            description: описание товара.
            price: цена товара.
            quantity: количество в наличии.
            efficiency: производительность.
            model: модель.
            memory: объём встроенной памяти.
            color: цвет.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Трава газонная — наследник класса Product.

    Attributes:
        country: страна-производитель.
        germination_period: срок прорастания.
        color: цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует газонную траву.

        Args:
            name: название товара.
            description: описание товара.
            price: цена товара.
            quantity: количество в наличии.
            country: страна-производитель.
            germination_period: срок прорастания.
            color: цвет.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
