from .vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, max_load: float):
        super().__init__(brand, model, year)
        self.max_load = max_load               #тонны

    def get_info(self) -> str:
        return f"{super().get_info()}, грузоподъёмность: {self.max_load} т"

    def move(self) -> str:
        return (f"{self.brand} {self.model} перевозит груз "
                f"до {self.max_load} т со скоростью {self.speed} км/ч.")   #Задание 7