import random
import os 
import pickle
import itertools
import time
# random function returns floating numbers between give range
# for i in range(5):
# 	print("%04.3f" % random.random(), end=" ")
# print()

# To generate numbers in specific numerical range, use uniform()
# for i in range(5):
# 	print('{:04.3f}'.format(random.uniform(0, 10)), end=" ")
# print()

# seed() 
# random.seed(1)

# for i in range(5):
# 	print("{:04.3f}".format(random.random()), end=" ")
# print()

# if os.path.exists('state.dat'):
# 	print("Found state.dat, initializing random module")
# 	with open('state.dat', 'rb') as f:
# 		state = pickle.load(f)
# 	random.setstate(state)
# else:
# 	print('No state.dat, seeding')
# 	random.seed(1)

# for i in range(3):
# 	print('{:04.3f}'.format(random.random()), end=" ")
# print()

# with open('state.dat', 'wb') as f:
# 	pickle.dump(random.getstate(), f)

# print("\n After saving state: ")
# for i in range(3):
# 	print("{:04.3f}".format(random.random()), end=' ')
# print()	

# randint() to generate integers directly 
# print('[1, 100]:', end=' ')

# for i in range(3):
# 	print(random.randint(1, 100), end=' ')

# print('\n[-5, 5]:', end=' ')
# for i in range(3):
# 	print(random.randint(-5, 5))
# print()

# randrange() is more form of selecting values from a range
# it is fully equialent to selecting a random value from(start, stop, step)

# for i in range(3):
# 	print(random.randrange(0, 101, 5), end=' ')
# print()

# choice() is used to select randomly any item from sequence
# outcomes = {
# 	'heads': 0,
# 	'tails': 0,
# }
# sides = list(outcomes.keys())

# for i in range(10000):
# 	outcomes[random.choice(sides)] += 1

# print('Heads:', outcomes['heads'])
# print("Tails:", outcomes['tails'])

# shuffle() 

# li = [1, 2, 3, 4, 5]
# random.shuffle(li)
# print(li)

# sample() function generates samples without repeating and 
# modifying the input sequence.

# li = [1, 2, 3, 4, 5, 6]
# print(random.sample(li, 3))

# print("Default initialization")

# r1 = random.Random()
# r2 = random.Random()

# for i in range(3):
# 	print("{:04.3f} {:04.3f}".format(r1.random(), r2.random()))
# print("\nSame seed:\n")

# seed = time.time()
# r1 = random.Random(seed)
# r2 = random.Random(seed)

# for i in range(3):
# 	print("{:04.3f} {:04.3f}".format(r1.random(), r2.random()))

# System.Random() 
print("Default initialization")

r1 = random.SystemRandom()
r2 = random.SystemRandom()

for i in range(3):
	print("{:04.3f} {:04.3f}".format(r1.random(), r2.random()))
print("\nSame seed:\n")

seed = time.time()
r1 = random.SystemRandom(seed)
r2 = random.SystemRandom(seed)

for i in range(3):
	print("{:04.3f} {:04.3f}".format(r1.random(), r2.random()))
