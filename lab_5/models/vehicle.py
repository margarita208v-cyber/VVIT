from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Базовый класс транспортного средства."""

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self._speed = 0          #Задание 2

   
    @property
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, value: int):
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self._speed = value                    #Задание 4

   
    def accelerate(self, value: int):
        self.speed = self.speed + value   # через setter

    def brake(self, value: int):
        self.speed = max(0, self.speed - value)  # не ниже нуля

    def stop(self):
        self.speed = 0           #Задание 3 и 4 

    def get_info(self) -> str:
        return (f"{self.brand} {self.model} ({self.year}), "
                f"скорость: {self.speed} км/ч")

    
    def __str__(self) -> str:
        return (f"{self.brand} {self.model}, {self.year} г., "
                f"{self.speed} км/ч")         #Задание 5


    @abstractmethod
    def move(self) -> str:
        """Каждый тип ТС реализует собственный способ движения."""  #Задание 8
