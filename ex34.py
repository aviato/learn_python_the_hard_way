animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
print 'These are the animals: ', animals

"""
1. The animal at 1.
2. The third (3rd) animal.
3. The first (1st) animal.
4. The animal at 3.
5. The fifth (5th) animal.
6. The animal at 2.
7. The sixth (6th) animal.
8. The animal at 4.

"""

print """

Here are the answers:
1. %s
2. %s
3. %s
4. %s
5. %s
6. %s
7. %s
8. %s
""" % (animals[1], animals[2], animals[0], animals[3], animals[4], animals[2], animals[5],
animals[3])