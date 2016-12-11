import re
from itertools import combinations

def is_valid_state(state):
	for floor in state[1]:
		generators = [g[0] for g in floor if g[1] == 1]
		chips = [c[0] for c in floor if c[1] == 0]
		if len(generators) > 0:
			for c in chips:
				if c not in generators:
					return False
	return True

def is_end_state(state):
	floors = state[1]
	return len(floors[0]) == len(floors[1]) == len(floors[2]) == 0

def get_state_format(state):
	global number_elements
	floors = state[1]
	item_states = [[0,0] for _ in range(number_elements)]
	for i, floor in enumerate(floors):
		for item in floor:
			item_states[item[0]][item[1]] = i
	return (state[0], tuple(sorted(map(tuple, item_states))))

def read_puzzle_input():
	puzzle_input = [re.findall('a (\w+)(?:-compatible)? (\w+)', line) for line in open('input.txt').readlines()]
	name_mapper = {}
	type_mapper = {'microchip': 0, 'generator': 1}
	number_elements = 0
	for i, line in enumerate(puzzle_input):
		new_line = []
		for item in line:
			if item[0] not in name_mapper:
				name_mapper[item[0]] = number_elements
				number_elements += 1
			new_line.append((name_mapper[item[0]], type_mapper[item[1]]))
		puzzle_input[i] = frozenset(new_line)

	return number_elements, tuple(puzzle_input)


number_elements, puzzle_input = read_puzzle_input()
elevator_start = 0
start_state = (elevator_start, puzzle_input)
state_queue = [(start_state, 0)]
visited_state_formats = {get_state_format(start_state)}

while True:
	state, steps = state_queue.pop(0)
	elevator, floors = state
	new_steps = steps + 1
	current_floor = floors[elevator]

	for items in list(combinations(current_floor, 2)) + list(combinations(current_floor, 1)):
		new_current_floor = frozenset(i for i in current_floor if i not in items)
		for direction in [1, -1]:
			target = elevator + direction
			if 0 <= target < 4:
				target_floor = floors[target] | frozenset(items)
				if direction == 1:
					new_floors = floors[:elevator] + (new_current_floor, target_floor) + floors[target+1:]
				else:
					new_floors = floors[:target] + (target_floor, new_current_floor) + floors[elevator+1:]
				new_state = (target, new_floors)
				if is_valid_state(new_state):
					if is_end_state(new_state):
						print new_steps
						exit()
					state_format = get_state_format(new_state)
					if state_format not in visited_state_formats:
						visited_state_formats.add(state_format)
						state_queue.append((new_state, new_steps))
