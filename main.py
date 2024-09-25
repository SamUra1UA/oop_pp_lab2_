class Car:
    def __init__(self, make, model, year):
        self._make = make  # Приватна властивість
        self._model = model  # Приватна властивість
        self.year = year  # Відкрита властивість

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    def car_info(self):
        return f"{self.year} {self._make} {self._model}"

    def start_engine(self):
        return f"Engine of {self._make} {self._model} started."

    @staticmethod
    def service_interval():
        return 10000  # Пробіг для технічного обслуговування (в км)

# Додатковий батьківський клас для множинного наслідування
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def battery_info(self):
        return f"Battery size: {self.battery_size} kWh"

    def charge_battery(self):
        return f"Battery charged to {self.battery_size} kWh."

# Дочірній клас ElectricCar (електромобіль)
class ElectricCar(Car, Battery):
    def __init__(self, make, model, year, battery_size=75):
        Car.__init__(self, make, model, year)
        Battery.__init__(self, battery_size)

    def start_engine(self):
        return f"{self._make} {self._model} is powered by electricity."

# Дочірній клас HybridCar (гібридний автомобіль)
class HybridCar(Car):
    def __init__(self, make, model, year, battery_size=40):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def start_engine(self):
        return f"{self._make} {self._model} uses both gasoline and electricity."

    def charge_battery(self):
        return f"Hybrid car's battery charged to {self.battery_size} kWh."

# Демонстраційний алгоритм роботи з класами
if __name__ == "__main__":
    # Створюємо екземпляр класу Car
    car = Car("Toyota", "Corolla", 2020)
    print(car.car_info())  # Виводимо інформацію про авто
    print(car.start_engine())  # Запускаємо двигун

    # Створюємо екземпляр класу ElectricCar
    electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
    print(electric_car.car_info())  # Виводимо інформацію про електромобіль
    print(electric_car.start_engine())  # Запускаємо електродвигун
    print(electric_car.charge_battery())  # Заряджаємо батарею

    # Створюємо екземпляр класу HybridCar
    hybrid_car = HybridCar("Toyota", "Prius", 2021)
    print(hybrid_car.car_info())  # Виводимо інформацію про гібрид
    print(hybrid_car.start_engine())  # Запускаємо гібридний двигун
    print(hybrid_car.charge_battery())  # Заряджаємо батарею

    # Використання поліморфізму
    cars = [car, electric_car, hybrid_car]
    for c in cars:
        print(c.start_engine())

    # Використання статичного методу
    print(f"Service interval: {Car.service_interval()} km")
