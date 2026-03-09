class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        return f"{self.brand} {self.model} is starting."

    def stop(self):
        return f"{self.brand} {self.model} is stopping."

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


# Child class 1
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def start(self):
        return f"{self.brand} {self.model} roars to life with {self.doors} doors!"

    def honk(self):
        return f"{self.brand} {self.model} goes 'Beep beep!'"

    def __str__(self):
        return f"{super().__str__()} with {self.doors} doors"


# Child class 2
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, type_motorcycle):
        super().__init__(brand, model, year)
        self.type_motorcycle = type_motorcycle

    def start(self):
        return f"{self.brand} {self.model} revs its engine!"

    def wheelie(self):
        return f"{self.brand} {self.model} is doing a wheelie!"

    def __str__(self):
        return f"{super().__str__()} ({self.type_motorcycle} bike)"