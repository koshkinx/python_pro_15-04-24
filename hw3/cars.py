import random


class Car:
    def __init__(self, model, color):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = 0
        self.model = model
        self.color = color

    def move(self, distance):
        self.trip_distance += distance
        self.fuel -= distance


car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Blue")
car3 = Car("Mercedes", "Black")


desired_dist = 100
race_dist = 0

while race_dist < desired_dist:
    for car in [car1, car2, car3]:
        car.move(random.randrange(0, 100))
        if car.trip_distance >= desired_dist:
            print(f"Переміг {car.color} {car.model} - {car.trip_distance} км")
            break
    race_dist = max(car.trip_distance for car in [car1, car2, car3])


for car in [car1, car2, car3]:
    print(f"{car.color} {car.model} проїхав {
          car.trip_distance} км і має {car.fuel} одиниць палива залишку")
