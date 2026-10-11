"""Модуль с общими абстрактными классами проекта."""

from abc import ABC


class BaseNamedEntity(ABC):
    """Абстрактный класс для сущностей, имеющих название.

    Общий родитель для классов Category (категория) и Order (заказ).
    """

    def __init__(self, name: str) -> None:
        """Сохраняет название сущности.

        Args:
            name: название сущности.
        """
        self.name = name
