##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## class Dog is-a object (instance of class Animal)
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name
		
## class Cat is-a object (instance of class Animal)
class Cat(Animal):

	def __init__(self, name):
		## class Cat has-a name
		self.name = name
		
## class Person is-a class(object)
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## class Employee is-a object (instance of class Person)
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
## class Fish is a class(object)
class Fish(object):
	pass

## class Salmon is-a Fish
class Salmon(Fish):
	pass
	
## class Halibut is-a Fish
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee(has-a 120000 salary)
frank = Employee("Frank", 120000)

## frank has-a pet 
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

