# SOLID Principles - Single Responsibility Principle (SRP) & Open/Closed Principle (OCP)
# This code demonstrates the Single Responsibility Principle (SRP) and Open/Closed Principle (OCP)


from abc import ABC, abstractmethod
class Car(ABC):
    def __init__(self,name,brand,year):
        self.name=name
        self.brand=brand
        self.year=year
        print(f"This {self.name} is my favorite {self.year} car and still my {self.year} car right now")
    @abstractmethod
    def favourite_car(self):
        pass
class suv(Car):
    def __init__(self,name,brand,year,type):
        self.type=type
        super().__init__(name,brand,year)
        print(f"This {self.name} is my favorite {self.year} car and {self.type} car right now")
    def favourite_car(self):
        print("I'm using the best car")
class sedan(Car):
    def favourite_car(self):
        print("My car is Nice")
class off_road(Car):
    def favourite_car(self):
        pass
def print_favourite_car(car:Car):
    car.favourite_car()
suv_car = suv("Nissan","Titan",2021,"Off Roader")
sedan_car= sedan("Honda","Accord",2022)
offroad_car=off_road("Ford","F-150",2025)
print_favourite_car(sedan_car)