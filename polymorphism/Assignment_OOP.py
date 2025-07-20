class Car:
    def __init__(self, model, brand):
        self. model = model
        self.brand = brand

    def move(self):
        print("Move!")

class Motor:
    def __init__(self, model, brand):
        self. model = model
        self.brand = brand
    def move(self):
        print("Ride!")
    
class Ship:
    def __init__(self, model, brand):
        self. model = model
        self.brand = brand
    def move(self):
        print("Sail!")


car1 = Car("Escape","Ford")
motor1 = Motor("Supersport", "Royal link")
ship1 = Ship("Sea Ray","Hundai")
car1.move()

for x in (car1,motor1,ship1):
     x.move()
