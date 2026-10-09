"""Модуль main — демонстрация работы классов интернет-магазина."""

from src.categories import Category
from src.products import LawnGrass, Product, Smartphone


def main() -> None:
    """Запускает демонстрацию работы классов Product и его наследников."""
    smartphone = Smartphone(
        "Samsung Galaxy S23", "Смартфон", 80000.0, 5, 3.2, "S23", 256, "серый"
    )
    lawn_grass = LawnGrass(
        "Газонная трава", "Семена газонной травы", 4500.0, 20, "Россия", "10 дней", "зелёный"
    )
    product = Product("Плодородный грунт", "Универсальный грунт", 500.0, 100)

    print("=== Товары ===")
    print(smartphone)
    print(lawn_grass)
    print(product)

    print("\n=== Категория ===")
    category = Category("Сад и электроника", "Разные товары", [])
    category.add_product(smartphone)
    category.add_product(lawn_grass)
    category.add_product(product)
    print(category)
    print(category.products)

    print("=== Сложение одинаковых классов ===")
    second_smartphone = Smartphone(
        "Apple iPhone 15", "Смартфон", 100000.0, 3, 3.5, "15", 128, "чёрный"
    )
    print("Сумма двух смартфонов:", smartphone + second_smartphone)

    print("\n=== Ограничение сложения ===")
    try:
        smartphone + lawn_grass
    except TypeError as error:
        print("Ошибка сложения:", error)

    print("\n=== Ограничение добавления в категорию ===")
    try:
        category.add_product("это не товар")
    except TypeError as error:
        print("Ошибка добавления:", error)


if __name__ == "__main__":
    main()
