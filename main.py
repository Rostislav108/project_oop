"""Модуль main — демонстрация работы классов интернет-магазина."""

from src.base import BaseNamedEntity
from src.categories import Category
from src.exceptions import ZeroQuantityError
from src.orders import Order
from src.products import BaseProduct, LawnGrass, Product, Smartphone


def main() -> None:
    """Запускает демонстрацию работы классов и обработку исключений."""
    print("=== Создание товаров (миксин печатает информацию) ===")
    smartphone = Smartphone(
        "Samsung Galaxy S23", "Смартфон", 80000.0, 5, 3.2, "S23", 256, "серый"
    )
    lawn_grass = LawnGrass(
        "Газонная трава", "Семена газонной травы", 4500.0, 20, "Россия", "10 дней", "зелёный"
    )
    product = Product("Плодородный грунт", "Универсальный грунт", 500.0, 100)

    print("\n=== Обработка нулевого количества (ValueError) ===")
    try:
        Product("Нулевой товар", "Описание", 100.0, 0)
    except ValueError as error:
        print("Ошибка:", error)

    print("\n=== Абстрактный класс BaseProduct ===")
    print("Абстрактные методы:", BaseProduct.__abstractmethods__)
    try:
        BaseProduct("Тест", "Описание", 100.0, 1)
    except TypeError as error:
        print("Объект абстрактного класса создать нельзя:", error)

    print("\n=== Категория и средний ценник ===")
    category = Category(
        "Сад и электроника", "Разные товары", [smartphone, lawn_grass, product]
    )
    print(category)
    print(f"Средний ценник: {category.average_price():.2f} руб.")

    empty_category = Category("Пустая категория", "Без товаров", [])
    print("Средний ценник пустой категории:", empty_category.average_price())

    print("\n=== Сложение одинаковых классов ===")
    second_smartphone = Smartphone(
        "Apple iPhone 15", "Смартфон", 100000.0, 3, 3.5, "15", 128, "чёрный"
    )
    print("Сумма двух смартфонов:", smartphone + second_smartphone)

    print("\n=== Ограничения ===")
    try:
        smartphone + lawn_grass
    except TypeError as error:
        print("Ошибка сложения:", error)

    print("\n=== Доп. задание: пользовательское исключение ===")
    product.quantity = 0
    try:
        category.add_product(product)
    except ZeroQuantityError as error:
        print("Ошибка:", error)
    else:
        print("Товар добавлен")
    finally:
        print("Обработка добавления товара завершена")

    product.quantity = 100
    try:
        category.add_product(product)
    except ZeroQuantityError as error:
        print("Ошибка:", error)
    else:
        print("Товар добавлен")

    print("\n=== Заказ (дополнительное задание) ===")
    order = Order("Заказ №1", smartphone, 2)
    print(f"{order.name}: {order.product.name} x {order.quantity} = {order.total_cost} руб.")
    print("Order — наследник BaseNamedEntity:", isinstance(order, BaseNamedEntity))


if __name__ == "__main__":
    main()
