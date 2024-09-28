from car import Car
from battery import Battery  # Використовуємо Battery для роботи з батареєю
from battery_chargeable import BatteryChargeable  # Інтерфейс для заряджання

class ElectricCar(Car, BatteryChargeable):
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def start_engine(self):
        return f"{self._make} {self._model} is powered by electricity."

    def charge_battery(self):
        return f"Electric car's battery charged to {self.battery_size} kWh."
