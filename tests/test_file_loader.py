"""Тесты загрузки категорий и товаров из JSON-файла."""

import json

from src.file_loader import load_categories_from_json


def test_load_categories_from_json(tmp_path) -> None:
    """Создаёт объекты Category и Product из JSON-файла."""
    data = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [
                {"name": "Samsung", "description": "256GB", "price": 180000.0, "quantity": 5}
            ],
        }
    ]
    file_path = tmp_path / "products.json"
    file_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    categories = load_categories_from_json(file_path)

    assert len(categories) == 1
    assert categories[0].name == "Смартфоны"
    assert categories[0].products[0].name == "Samsung"
    assert categories[0].products[0].price == 180000.0
    assert categories[0].products[0].quantity == 5
