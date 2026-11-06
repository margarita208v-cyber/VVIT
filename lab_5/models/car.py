from .vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, doors: int):
        super().__init__(brand, model, year)   #общая часть
        self.doors = doors                     

    def get_info(self) -> str:
        return f"{super().get_info()}, дверей: {self.doors}"

    def move(self) -> str:
        return f"{self.brand} {self.model} едет по дороге на {self.speed} км/ч."   #Задание 6