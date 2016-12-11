import re
from itertools import combinations

def is_valid_state(state):
	for floor in state[1]:
		generators = [g[0] for g in floor if g[1] == 'generator']
		chips = [c[0] for c in floor if c[1] == 'microchip']
		if len(generators) > 0:
			for c in chips:
				if c not in generators:
					return False
	return True

def is_end_state(state):
	floors = state[1]
	return len(floors[0]) == len(floors[1]) == len(floors[2]) == 0

puzzle_input = tuple(frozenset(re.findall('a (\w+)(?:-compatible)? (\w+)', line)) for line in open('input.txt').readlines())
elevator_start = 0
start_state = (elevator_start, puzzle_input)
state_queue = [(start_state, 0)]
visited_states = {start_state}

while True:
	state, steps = state_queue.pop(0)
	elevator, floors = state
	new_steps = steps + 1
	current_floor = floors[elevator]
	for items in list(combinations(current_floor, 1)) + list(combinations(current_floor, 2)):
		new_current_floor = frozenset(i for i in current_floor if i not in items)
		if elevator > 0:
			target = elevator - 1
			target_floor = floors[target] | frozenset(items)
			new_floors = floors[:target] + (target_floor, new_current_floor) + floors[elevator+1:]
			new_state = (elevator-1, new_floors)
			if is_valid_state(new_state):
				if is_end_state(new_state):
					print new_steps
					exit()
				if new_state not in visited_states:
					visited_states.add(new_state)
					state_queue.append((new_state, new_steps))

		if elevator < 3:
			target = elevator + 1
			target_floor = floors[target] | frozenset(items)
			new_floors = floors[:elevator] + (new_current_floor, target_floor) + floors[target+1:]
			new_state = (elevator+1, new_floors)
			if is_valid_state(new_state):
				if is_end_state(new_state):
					print new_steps
					exit()
				if new_state not in visited_states:
					visited_states.add(new_state)
					state_queue.append((new_state, new_steps))
