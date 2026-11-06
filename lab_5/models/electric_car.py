from .car import Car


class ElectricCar(Car):
    def __init__(self, brand: str, model: str, year: int,
                 doors: int, battery_kwh: float, range_km: int):
        super().__init__(brand, model, year, doors)   
        self.battery_kwh = battery_kwh
        self.range_km = range_km

    def get_info(self) -> str:
        return (f"{super().get_info()}, батарея: {self.battery_kwh} кВт·ч, "
                f"запас хода: {self.range_km} км")

    def move(self) -> str:
        return (f"{self.brand} {self.model} (электро) бесшумно едет "
                f"на {self.speed} км/ч, запас хода {self.range_km} км.")    #Задание 12 сам но
    