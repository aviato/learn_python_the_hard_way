Ífrom sys import argv

script, first, second, third, new_var = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

new_var = raw_input("Enter something cool...")

print "Your fourth variable is:", new_var