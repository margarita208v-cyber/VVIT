from models.vehicle import Vehicle


class Garage:
   
    def __init__(self):
        self.vehicles: list[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("В гараж можно добавлять только Vehicle")
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def show_all(self):
        if not self.vehicles:
            print("Гараж пуст.")
            return
        print("=== Содержимое гаража ===")
        for i, v in enumerate(self.vehicles, 1):
            print(f"{i}. {v.get_info()}")

    def find_by_brand(self, brand: str) -> list[Vehicle]:
        return [v for v in self.vehicles
                if v.brand.lower() == brand.lower()]       #Задание 10