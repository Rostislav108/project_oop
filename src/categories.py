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
            Строка, в которой каждый товар записан по шаблону
            «Название продукта, X руб. Остаток: X шт.».
        """
        return "".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            for product in self.__products
        )
