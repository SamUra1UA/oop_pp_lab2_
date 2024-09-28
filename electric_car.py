from car import Car
from battery import Battery

class ElectricCar(Car, Battery):
    def __init__(self, make, model, year, battery_size=75):
        Car.__init__(self, make, model, year)
        Battery.__init__(self, battery_size)

    def start_engine(self):
        return f"{self._make} {self._model} is powered by electricity."
