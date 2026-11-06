from .vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, year: int, has_sidecar: bool):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar         #коляска
    
    def get_info(self) -> str:
        sidecar = "с коляской" if self.has_sidecar else "без коляски"
        return f"{super().get_info()}, {sidecar}"

    def move(self) -> str:
        return (f"{self.brand} {self.model} мчится на {self.speed} км/ч "
                f"({ 'с коляской' if self.has_sidecar else 'без коляски'}).")   #Задание 7