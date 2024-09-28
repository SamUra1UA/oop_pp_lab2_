from abc import ABC, abstractmethod

class BatteryChargeable(ABC):
    @abstractmethod
    def charge_battery(self):
        """Абстрактний метод для заряджання батареї"""
        pass
