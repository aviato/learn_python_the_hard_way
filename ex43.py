from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		print "Engine __init__ has scene_map", scene_map
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		print "Play's first scene", current_scene
		
		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			print "next scene", next_scene_name
			current_scene = self.scene_map.next_scene(next_scene_name)
			print "map returns new scene", current_scene
		
# Death (Scene)
class Death(Scene):
	
	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a luser.",
		"I have a small puppy that's better at this."
		]
		
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

# Central Corridor (Scene)
class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it inn the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps outred scaly skin, dark grimy teeth, and evil clowncostume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."
		
		action = raw_input("> ")
		
		if action == "shoot!":
			print "Quick on the draw, you yank out your blaster and fire at Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume his mother bought him,"
			print "which makes him fly into an insane rage and blast you repeatedly in"
			print "the face until you are dead. Then he eats you."
			return 'death'
			
		elif action == 'dodge!':
			print "like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on your"
			print "head and eats you."
			return 'death'
			
		elif action == "tell a joke":
			print "lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "LBHE ZBGURE VF FB SNG, JURA FUR FVGF NEBH AQ GUR UBHFR, FUR FVGF"
			print "NEBHAQ GUR UBHFR."
			print "The Gothon stops, tries not to laugh, the Gothon busts out laughing"
			print "and can't move. While he's laughing you run up and shoot him"
			print "square in the head, puttting him down, the jump through the Weapon"
			print "Armory door."
			return 'laser_weapon_armory'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'
			
# Laser Weapon Armory (Scene)
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive roll innto the Weapon Armory, crouch, and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in it's container. There's a key pad lock on the box"
		print "and you need the code to get the bomb out. If you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get the bomb then lock closes forever and you can't get the bomb."
		print "the code is 3 digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess!= code and guesses < 10:
			print "BZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")
		
		if guess == code:
			print "The container clicks opena nd the seal breaks, letting gas out."
			print "you grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		
		else:
			print "The lock buzzes one last time and then you hear a sickening melting"
			print "sound as the mechanism is fused together. You decide to sit there, and"
			print "finally the Gothons blow up the ship from their ship and you die."
			return 'death'
		
# The Bridge (Scene)
class TheBridge(Scene):

	def enter(self):
		print "You burst onto the Bridge with the neutron destruct bomb"
		print "under your arm and surprise the 5 Gothons who are trying to take control"
		print "of the ship. Each of them has an even uglier clown costume than the"
		print "last. They haven't pulled their weapons out yet, as they see the active"
		print "bomb under your arm and don't want to set it off"
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons and make a"
			print "leap for the door. Right as you drop it a Gothon shoots you right in"
			print "the back killing you. As you die you see another Gothon frantically"
			print "try to disarm the bomb. You die knowing they will probably blow up"
			print "when it goes off."
			return 'death'
			
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm and the Gothons put"
			print "their hands up and start to sweat. You inch backward to the door, "
			print "open it, and then carefully place the bomb on the floor, pointing your"
			print "blaster at it. You then jump back through the door, punch the close "
			print "button, and blast the lock so the Gothons can't get out. Now that the"
			print "bomb is placed you run to the escape pod to get off this tin can."
			return 'escape_pod'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'the_bridge'

# Escape Pod (Scene)
class EscapePod(Scene):

	def enter(self):
		print "You rush through the ship desperately trying to make it to the escape"
		print "pod before the whole ship explodes. It seems like hardly any Gothons are"
		print "on the ship, so your run is clear of interference. You get to the"
		print "chamber with the escape pods, and now need to pick one to take. Some of"
		print "them could be damaged, but you don't have time to look. There's 5 pods,"
		print "which one do you take?"
		
		good_pod = randint(1, 5)
		guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod escapes out into the void of space, then implodes as the hull"
			print "ruptures, crushing your body into jam jelly."
			return 'death'
			
		else:
			print "You jump into the pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to the planet below."
			print "As it flies to the planet, you look back and see your ship implode"
			print "then explode like a bright star, taking out the Gothon ship at the"
			print "same time. You won!"
			
			return 'finished'
			
				
# uses dict. (scenes) as way to organize the different scenes
class Map(object):

	scenes = {
		'death': Death(),
		'central_corridor': CentralCorridor(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		print "start_scene in __init__", self.start_scene
				
	def next_scene(self, scene_name):
		print "start_scene in the next_scene"
		val = Map.scenes.get(scene_name)
		print "next_scene returns", val
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		


# Load Map, Engine, and play game...		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()