from random import randint
from sys import exit

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Engine(object):
	pass
	
	
class Map(object):
	pass
	
	
class Room(object):
	pass
	

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Char(object):
	def __init__(self, name, hp, weapon, dmg_max):
		self.name = name
		self.hp = hp
		self.weapon = weapon
		self.dmg_max = dmg_max
		
	def who_am_i(self):
		print "I am %s! I have %i hitpoints remaining!" % (self.name, self.hp)
		print "My weapon is %s that does %i damage!" % (self.weapon, self.dmg_max)


class Hero(Char):
	pass
	
class Enemy(Char):
	pass
	

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ryan = Hero("Ryan", 100, "2h Sword", 15)
dragon = Enemy("Dragon", 100, "Large talons", 15)
Hero.who_am_i(ryan)
Enemy.who_am_i(dragon)