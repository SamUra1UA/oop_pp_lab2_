class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self.year = year

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
        raise NotImplementedError("This method should be overridden in subclasses")
