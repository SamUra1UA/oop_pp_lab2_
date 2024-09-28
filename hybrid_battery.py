from battery_chargeable import BatteryChargeable

class HybridBattery(BatteryChargeable):
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def charge_battery(self):
        return f"Hybrid car's battery charged to {self.battery_size} kWh."
