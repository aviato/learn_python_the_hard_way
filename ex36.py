#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~LPTHW ex. 35~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~Made by Ryan S. Price~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~This shitty version: v.8/10/14~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from sys import exit
from random import randint





#~~~~~~~~~~~~~~~~~~~~~~~~~Start~~~~~~~~~~~~~~~~~~~~~~~~~~~

def start():
  print "\n \nGreetings, Traveler! You have reached your destination!"
  print "The treasure you seek lies within the chambers of this cave."
  print "This has been the dragons lair for an age, so proceed with caution."
  print "Good luck to you!"
  print "\n \n"
  
  choose = raw_input("Press enter to continue! \n \n")
  choose.lower()
  
  while True:
    if choose == "enter":  lobby()
    elif len(choose) < 1:  choose = "enter"
    else:
      print "Oops! Press enter to continue! \n"
      start()
    
    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~Lobby~~~~~~~~~~~~~~~~~~~~~~~~~~~

def lobby():

  print "\nThere are three doors: the North Door, the East Door, and the West Door. \n"
  choose = raw_input("Which door do you choose? ")
  
  while True:
  
    if "north" in choose:
      treasure_room()
      
    elif "east" in choose:
    
      if "moon_key" in inventory:
      
        print "You have already defeated the troll."
        lobby()
        
      else:
        troll_room()
        
    elif "west" in choose:
    
      if "sun_key" in inventory:
      
        print "You have already killed the dragon."
        lobby()
        
      else:
        dragon_room()
        
    else:
      print "\nMake your choice, Traveler!"
      lobby()
    

    
#~~~~~~~~~~~~~~~~~~~~~~~~~Troll_Room~~~~~~~~~~~~~~~~~~~~~~~~~~~
# the riddle functions now call themselves 
def troll_room():

  print "\n \nYou enter a dark, cavernous room with a strange smell."
  print "The floor is littered with bones and old tomes."
  print "You hear a faint sniffing, followed by the sound of menacing laughter.\n"
  print "Troll: 'You sought the dragon, did ye? Well I'm no dragon, as you can see.'"
  print "Troll: 'There may yet be a dragon here, but tis' I you must now fear.'"
  print "Troll: 'I am the troll of elder lore, and my task is now your chore.'"
  print "Troll: 'Solve these riddles, fail and die.'"
  print "Troll: '...should you succeed, your death becomes mine!'"   
  riddle1()


  
  
def riddle1():

  print "\n \nTroll: 'When you have me, you want to share me.'"
  print "Troll: 'When you share me, I no longer exist.'"
  
  answer = raw_input("Troll: 'What am I?' \n")
  
  if "secret" in answer:
    print "\nTroll: 'That one was easy! Try this one!'"
    riddle2()
  else:
    death("The troll ate you.")
    
    
def riddle2():

  print "\nTroll: 'In what way does 4 make half of five?'"
  
  answer = raw_input("Troll: 'What say you??' ")
  
  if "iv" in answer:
    print "\nTroll: 'You worthless little SHITE.'"
    print "\nTroll: 'Oh well, you'll never solve my final riddle! Muwhahahahah!'"
    riddle3()
  else:
    death("The troll ate you.")
        
def riddle3():

  print "\nTroll: 'What is brown and sticky?'"
  answer = raw_input("Troll: 'You'll never solve this one!' \n")
  
  if "stick" in answer:
    print "\nTroll: 'GAHHHH! IMPOSSIBLE!'"
    print "You defeated the Troll! You recieved the Moon Key."
    
    inventory.append("moon_key")
    print inventory
    lobby()
    
  else:
    death("The troll ate you.")
    

#~~~~~~~~~~~~~~~~~~~~~~Dragon Room~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def dragon_room():
  dragon_hp = 50
  print "\nThe stench of death is close, and hangs heavy in this dark, humid room."
  print "Sweat drips from your forehead and lands on your armor."
  print "It is dark, and you can faintly make out the shape of a chair."
  print "The glimmering golden throne seems to make the dark cave wall behind move."
  print "Wait... that isn't the wall! It's a dragon! To battle!!\n"
  
  print "\nThe dragon breathes fire toward you!"

  
  while True:
  
    damage = randint(5, 15)
    print "You unleash an attack! You did %r damage!\n" % damage
    dragon_hp = dragon_hp - damage
    print "The dragon has %r hp remaining!\n" % dragon_hp
    
    # dragon fire
    chance = randint(0, 100)
    if chance < 99:
      print "You dodged the attack!\n"
    else:
      death("You did not survive the attack.")
      
    if dragon_hp <= 0:
      print "The dragon has fallen! You received the sun_key! \n"
      inventory.append("sun_key")
      print inventory
      lobby()

    
    else:
      print "The dragon still lives. Keep fighting!\n"
      
#~~~~~~~~~~~~~~~~~~~~~Treasure_Room~~~~~~~~~~~~~~~~~~~~~~~~~~~
# known bug, after receiving the moon_key you can go straight
# to the treasure room

def treasure_room():

  if "sun_key" and "moon_key" in inventory:
    print "\n \nYou have entered the treasure chamber"
    print "Before you lie precious gems, and artifacts of ancient wonder."
    print "You have reached the end of your journey."
    print "You won!"
    print "Made by Ryan S. Price\n"
    
    exit(0)
    
  else:
  
    print "\n \nThe North Door has two ornate, emblazoned locks. \n"
    print "One lock has a faded painting of the Sun."
    print "The other lock has a dusty old painting of the Moon. \n"
    print "Find the keys to unlock the North Door!"
    
    lobby()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~Death~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def death(reason):

  print reason, "Try Again!"
  
  exit(0)
  
  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~GAME~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
inventory = []

start()
print "Inside the mouth of the cave is an ornate room."
