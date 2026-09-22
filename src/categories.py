"""Модуль с классом Category."""

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
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
