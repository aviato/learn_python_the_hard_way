# default value of i is 0...
i = 0
numbers = []
# ^ empty list to send values to...


# delimiter of '< 6'
while i < 6:
  print "At the top i is %d" % i
  # add 'i' to list 'numbers' every time loop iterates
  numbers.append(i)
  
  # add one to 'i', total of 'i' increments by 1...
  i = i + 1
  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i
  
  
print "The numbers: "

# print every number in 'numbers'
for num in numbers:
  print num