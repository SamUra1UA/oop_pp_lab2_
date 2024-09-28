from car import Car
from battery_chargeable import BatteryChargeable

class HybridCar(Car, BatteryChargeable):
    def __init__(self, make, model, year, battery_size=40):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def start_engine(self):
        return f"{self._make} {self._model} uses both gasoline and electricity."
