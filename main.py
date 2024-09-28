from electric_car import ElectricCar
from hybrid_car import HybridCar

if __name__ == "__main__":
    # Створюємо екземпляр класу ElectricCar
    electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
    print(electric_car.car_info())
    print(electric_car.start_engine())
    print(electric_car.charge_battery())  # Викликаємо метод charge_battery

    # Створюємо екземпляр класу HybridCar
    hybrid_car = HybridCar("Toyota", "Prius", 2021)
    print(hybrid_car.car_info())
    print(hybrid_car.start_engine())
    print(hybrid_car.charge_battery())  # Викликаємо метод charge_battery

    # Поліморфізм у дії
    cars = [electric_car, hybrid_car]
    for car in cars:
        print(car.start_engine())
        print(car.charge_battery())  # Всі машини можуть заряджати батарею
