from car import Car
from electric_car import ElectricCar
from hybrid_car import HybridCar

if __name__ == "__main__":
    # Створюємо екземпляр класу Car
    car = Car("Toyota", "Corolla", 2020)
    print(car.car_info())

    # Створюємо екземпляр класу ElectricCar
    electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
    print(electric_car.car_info())
    print(electric_car.start_engine())
    print(electric_car.charge_battery())

    # Створюємо екземпляр класу HybridCar
    hybrid_car = HybridCar("Toyota", "Prius", 2021)
    print(hybrid_car.car_info())
    print(hybrid_car.start_engine())
    print(hybrid_car.charge_battery())

    # Використання поліморфізму
    cars = [car, electric_car, hybrid_car]
    for c in cars:
        try:
            print(c.start_engine())
        except NotImplementedError:
            print(f"Engine not implemented for {c.car_info()}")

    # Використання статичного методу
    print(f"Service interval: {Car.service_interval()} km")
