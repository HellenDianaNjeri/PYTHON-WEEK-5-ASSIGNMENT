class Vehicle:
    def move(self):
        raise NotImplementedError("Each subclass must implement this method.")

class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying through the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing across the water 🚤"

class Train(Vehicle):
    def move(self):
        return "Chugging along the tracks 🚆"

def show_movement(vehicle):
    print(vehicle.move())

# Create objects of each type
car = Car()
plane = Plane()
boat = Boat()
train = Train()

# Call move() polymorphically
for v in [car, plane, boat, train]:
    show_movement(v)
