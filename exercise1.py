import random


class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0

    def flight_length(self):
        return random.randint(1, 10)

    def get_flight(self):
        return myinsect.flight_length


myinsect = Insect()

print("This insect can fly " + str(myinsect.flight_length()) + " miles.")
