# ex20.py: Functions and Files

# imports argv from command line

from sys import argv


# first argv = script, second = input_file

script, input_file = argv


# function called 'print_all' takes one para (f):
def print_all(f):
    print f.read()
# prints f.read [which will display the file]

    
# function 'rewind' also takes (f) as an arg...
def rewind(f):
    f.seek(0)
# applies the 'seek' method to f with 0 as an arg...

    
# function that prints 'line_count' and f.readline()
def print_a_line(line_count, f):
    print line_count, f.readline()


# var that opens 'input_file'
current_file = open(input_file)


# prints string
print "First let's print the whole file:\n"


# calling print_all with (current_file) as arg
print_all(current_file)


# prints string
print "Now let's rewind, kind of like a tape."


# calls rewind function with (current_file) as arg
rewind(current_file)


# prints string
print "Let's print three lines:"


# var current_line set to 1
current_line = 1


# print_a_line functions with two args
print_a_line(current_line, current_file)


# current_line updated... most likely to iterate
current_line = current_line + 1


print_a_line(current_line, current_file)


current_line = current_line + 1
print_a_line(current_line, current_file)