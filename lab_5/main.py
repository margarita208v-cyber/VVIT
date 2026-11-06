from models import Vehicle, Car, Truck, Motorcycle, ElectricCar
from garage import Garage


def main():
    print("--- Задание 8: попытка создать Vehicle напрямую ---")
    try:
        v = Vehicle("Generic", "X", 2020)
    except TypeError as e:
        print(f"Ожидаемая ошибка: {e}")
    print()

    print("--- Задание 6: Car ---")
    car = Car("Dodge", "Challenger", 2008, doors=4)
    print(car.get_info())
    car.accelerate(653)
    print(car.get_info())
    car.brake(3456789)        # скорость не станет отрицательной
    print(car.get_info())
    car.stop()
    print(car.get_info())
    print(car)            # __str__
    print()

    print("--- Задание 4: попытка задать отрицательную скорость ---")
    try:
        car.speed = -10
    except ValueError as e:
        print(f"Ожидаемая ошибка: {e}")
    print()

    truck = Truck("Haval", "Jolion", 2019, max_load=20.0)
    moto = Motorcycle("BMW", "Motorrad", 2021, has_sidecar=False)
    ev = ElectricCar("Tesla", "Model 3", 2023, doors=4,
                     battery_kwh=75.0, range_km=560)

    vehicles = [car, truck, moto, ev]

    print("--- Задание 9: полиморфный вызов move() и get_info() ---")
    for v in vehicles:

        v.accelerate(50)
        print(v.move())
        print(v.get_info())
    print()

    print("--- Задание 10: Garage ---")
    garage = Garage()
    for v in vehicles:
        garage.add_vehicle(v)

    garage.show_all()
    print()

    print("--- Поиск по марке 'Tesla' ---")
    for v in garage.find_by_brand("Tesla"):
        print(v.get_info())
    print()

    print("--- Удаление Truck из гаража ---")
    garage.remove_vehicle(truck)
    garage.show_all()


if __name__ == "__main__":
    main()