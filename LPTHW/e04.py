# -*- coding: utf-8 -*-
'''Variables and Names

'''


cars = 100
space_in_a_car = 4.0  # 4.0 is a floating number
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars avilable")
print("There are only", cars_driven, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
