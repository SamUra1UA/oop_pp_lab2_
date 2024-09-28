class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def battery_info(self):
        return f"Battery size: {self.battery_size} kWh"
