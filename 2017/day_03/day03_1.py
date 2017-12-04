def get_coords(target_value):
	if target_value == 1:
		return [0,0]

	coordinates = [1,0]
	value = 2
	size = 1

	while (size+2) ** 2 + 1 <= target_value:
		size += 2
		value = size ** 2 + 1
		coordinates = [(size-1)/2 + 1, (size-1)/2]

	# -y direction
	i = 0
	while i < size and value < target_value:
		i += 1
		value += 1
		coordinates[1] -= 1
	size += 1

	# -x direction
	i = 0
	while i < size and value < target_value:
		i += 1
		value += 1
		coordinates[0] -= 1

	# +y direction
	i = 0
	while i < size and value < target_value:
		i += 1
		value += 1
		coordinates[1] += 1

	# +x direction
	i = 0
	while i < size and value < target_value:
		i += 1
		value += 1
		coordinates[0] += 1

	return coordinates

def manhattan_distance(coords):
	return sum(map(abs, coords))


def required_steps(target_value):
	coords = get_coords(target_value)
	return manhattan_distance(coords)

puzzle_input = 289326
print required_steps(puzzle_input)
