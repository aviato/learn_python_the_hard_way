#imports argv commands from system
from sys import argv

#these are the arguments you can pass via argv in the command line
script, filename = argv

#var 'txt' uses the built in function 'open' with 'filename' as a parameter
txt = open(filename)

#
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("***")

txt_again = open(file_again)


print txt_again.read()