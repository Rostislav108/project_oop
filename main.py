"""Модуль main — демонстрация работы классов интернет-магазина."""

from src.base import BaseNamedEntity
from src.categories import Category
from src.orders import Order
from src.products import BaseProduct, LawnGrass, Product, Smartphone


def main() -> None:
    """Запускает демонстрацию работы классов и их ограничений."""
    print("=== Создание товаров (миксин печатает информацию) ===")
    smartphone = Smartphone(
        "Samsung Galaxy S23", "Смартфон", 80000.0, 5, 3.2, "S23", 256, "серый"
    )
    lawn_grass = LawnGrass(
        "Газонная трава", "Семена газонной травы", 4500.0, 20, "Россия", "10 дней", "зелёный"
    )
    product = Product("Плодородный грунт", "Универсальный грунт", 500.0, 100)

    print("\n=== Абстрактный класс BaseProduct ===")
    print("Абстрактные методы:", BaseProduct.__abstractmethods__)
    try:
        BaseProduct("Тест", "Описание", 100.0, 1)
    except TypeError as error:
        print("Объект абстрактного класса создать нельзя:", error)

    print("\n=== Категория ===")
    category = Category(
        "Сад и электроника", "Разные товары", [smartphone, lawn_grass, product]
    )
    print(category)
    print(category.products)

    print("=== Сложение одинаковых классов ===")
    second_smartphone = Smartphone(
        "Apple iPhone 15", "Смартфон", 100000.0, 3, 3.5, "15", 128, "чёрный"
    )
    print("Сумма двух смартфонов:", smartphone + second_smartphone)

    print("\n=== Ограничения ===")
    try:
        smartphone + lawn_grass
    except TypeError as error:
        print("Ошибка сложения:", error)
    try:
        category.add_product("это не товар")
    except TypeError as error:
        print("Ошибка добавления:", error)

    print("\n=== Заказ (дополнительное задание) ===")
    order = Order("Заказ №1", smartphone, 2)
    print(f"{order.name}: {order.product.name} x {order.quantity} = {order.total_cost} руб.")
    print("Order — наследник BaseNamedEntity:", isinstance(order, BaseNamedEntity))
    print("Category — наследник BaseNamedEntity:", isinstance(category, BaseNamedEntity))


if __name__ == "__main__":
    main()
