#var car = 100
cars = 100
#4.0 spaces in a car
space_in_a_car = 4.0
#30 drivers
drivers = 30
#90 passengers
passengers = 90
#var is equal to 100 - 30... should equal 70
cars_not_driven = cars - drivers
#cars_driven should equal 30
cars_driven = drivers
#c_c should equal 30 * 4... 120
carpool_capacity = cars_driven * space_in_a_car
#a_p_p_c should equal 90 / 30... or 3...	
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."