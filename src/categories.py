"""Модуль с классом Category."""

from typing import cast

from src.products import Product


class Category:
    """Категория товаров интернет-магазина.

    Attributes:
        category_count: общее количество созданных категорий.
        product_count: общее количество товаров во всех категориях.
    """

    category_count = 0
    product_count = 0

    def __init__(
        self, name: str, description: str, products: list[Product]
    ) -> None:
        """Инициализирует категорию.

        Args:
            name: название категории.
            description: описание категории.
            products: список товаров категории (объекты класса Product).
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в приватный список товаров категории.

        Args:
            product: объект класса Product для добавления.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает строку со всеми товарами категории.

        Returns:
            Строка, в которой каждый товар записан на отдельной строке.
        """
        return "".join(f"{product}\n" for product in self.__products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории.

        Returns:
            Строка вида «Название категории, количество продуктов: X шт.»,
            где количество считается как общее число товаров на складе.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    """Вспомогательный класс для перебора товаров категории.

    Позволяет перебирать товары категории в цикле for.
    """

    def __init__(self, category: Category) -> None:
        """Сохраняет список товаров категории для перебора.

        Args:
            category: категория, товары которой нужно перебирать.
        """
        self._products = cast(
            list[Product], getattr(category, "_Category__products")
        )
        self._index = 0

    def __iter__(self) -> "CategoryIterator":
        """Сбрасывает индекс и возвращает итератор."""
        self._index = 0
        return self

    def __next__(self) -> Product:
        """Возвращает очередной товар категории."""
        if self._index >= len(self._products):
            raise StopIteration
        product = self._products[self._index]
        self._index += 1
        return product
