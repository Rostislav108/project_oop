"""Модуль для загрузки категорий и товаров из JSON-файла."""

import json
from pathlib import Path
from typing import Any

from src.categories import Category
from src.products import Product

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PRODUCTS_FILE = PROJECT_ROOT / "data" / "products.json"


def load_categories_from_json(file_path: str | Path = DEFAULT_PRODUCTS_FILE) -> list[Category]:
    """Читает JSON-файл и создаёт объекты классов Category и Product.

    Args:
        file_path: путь к JSON-файлу с категориями и товарами.

    Returns:
        Список объектов класса Category, в каждом из которых
        список объектов класса Product.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data: list[dict[str, Any]] = json.load(file)

    categories = []
    for item in data:
        products = [
            Product(
                name=product["name"],
                description=product["description"],
                price=float(product["price"]),
                quantity=int(product["quantity"]),
            )
            for product in item.get("products", [])
        ]
        categories.append(
            Category(
                name=item["name"],
                description=item["description"],
                products=products,
            )
        )
    return categories
