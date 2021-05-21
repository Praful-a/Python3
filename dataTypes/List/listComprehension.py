# matrix = []
# for i in range(5):
# 	# Append an empty sublist inside the list
# 	matrix.append([])
# 	for j in range(5):
# 		matrix[i].append(j)

# print(matrix)

# Nested list comprehension
# matrix = [[j for j in range(5)] for i in range(5)]
# print(matrix)


# 2-D List
# matrix = [[1, 2, 3], [4, 5], [6,7, 8, 9]]

# flatten_matrix = []

# for sublist in matrix:
# 	for val in sublist:
# 		flatten_matrix.append(val)
# print(flatten_matrix)

# 2-D List of planets
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
# flatten_matrix = []

# for sublist in planets:
# 	for val in sublist:
# 		if (len(val) < 6):
# 			flatten_matrix.append(val)
# print(flatten_matrix)

# using list comprehension
flatten_planets = [planet for sublist in planets for planet in sublist if (len(planet) < 6)]
print(flatten_planets)