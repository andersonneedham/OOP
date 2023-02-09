import InsectClass as i

wings = 2
legs = 4


bug1 = i.Insect("mosquito", wings, legs)
bug2 = i.Insect("housefly", wings, legs)

bug1.flight_length()
bug2.flight_length()

print(f"The {bug1.get_name()} can fly up to {bug1.get_flight()}")
print(f"The {bug2.get_name()} can fly up to {bug2.get_flight()}")
