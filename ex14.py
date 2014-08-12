#imports module 'argv' from 'system'
from sys import argv

#arguments to be unpacked via module 'script, argv'
script, user_name = argv

#prompt = variable (str)
prompt = '*^*^*^*^*'

#section where we print several strings, passing in our variable imported ala 'argv'
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)