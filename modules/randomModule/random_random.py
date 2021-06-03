import random
import os
import pickle
import itertools

# for i in range(5):
#     print('%04.3f' % random.random(), end=' ')
# print()

# To generate numbers in a specific numerical range, use 
# uniform() instead.

# for i in range(5):
# 	print("{:04.3f}".format(random.uniform(1, 100)), end=" ")
# print()

# It produces the same value every time
# random.seed(1)

# for i in range(5):
# 	print("{:04.3f}".format(random.random()), end=" ")
# print()


# randint() to generate integers directly is more convenient

# print('[1, 100]:', end=' ')

# for i in range(3):
# 	print(random.randint(1, 100), end=' ')

# print('\n[-5, 5]:', end=" ")
# for i in range(3):
# 	print(random.randint(-5, 5), end=' ')
# print()

# randrange() is a more general form of selecting values from a range
# for i in range(3):
# 	print(random.randrange(0, 101, 5), end=" ")
# print()

# outcomes = {
# 	'heads': 0,
# 	'tails': 0,
# }
# sides = list(outcomes.keys())

# for i in range(10000):
# 	outcomes[random.choice(sides)] += 1

# print('Heads:', outcomes['heads'])
# print('Tails:', outcomes['tails'])

# FACE_CARDS = ('J', 'Q', 'K', 'A')
# SUITS = ('H', 'D', 'C', 'S')

# def new_deck():
# 	return [ '{:>2}{}'.format(*c)
# 		for c in itertools.product(
# 			itertools.chain(range(2, 11), FACE_CARDS),
# 			SUITS,)
# 	]

# def show_deck(deck):
# 	p_deck = deck[:]
# 	while p_deck:
# 		row = p_deck[:13]
# 		p_deck = p_deck[13:]
# 		for j in row:
# 			print(j, end=" ")
# 		print()

# # Make a new deck, with the cards in order
# deck = new_deck()
# print("Initial deck:")
# show_deck(deck)

# # Shuffle the deck to randomize the order
# random.shuffle(deck)
# print("\nShuffled deck:")
# show_deck(deck)

# # Deal 4 hands of 5 cards each
# hands = [[], [], [], []]

# for i in range(5):
# 	for h in hands:
# 		h.append(deck.pop())

# # show the hands
# print("\nHands:")
# for n, h in enumerate(hands):
# 	print("{}:".format(n+1), end=' ')
# 	for c in h:
# 		print(c, end=" ")
# 	print()

# # show the remaining deck
# print("\nRemaining deck:")
# show_deck(deck)

import time

print("Default initialization:\n")

r1 = random.SystemRandom()
r2 = random.SystemRandom()

for i in range(3):
	print("{:04.3f} {:04.3f}".format(r1.random(), r2.random()))

print("\nSame seed:\n")

seed = time.time()

r1 = random.SystemRandom(seed)
r2 = random.SystemRandom(seed)

for i in range(3):
	print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))

