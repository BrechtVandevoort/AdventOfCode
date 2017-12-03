puzzle_input = 3014387
elves = [i for i in xrange(1, puzzle_input + 1)]

start_pos = 0
while len(elves) > 1:
	is_odd = len(elves) % 2
	if start_pos == 1:
		elves = elves[1::2]
		if is_odd:
			start_pos = 0

	else:
		elves = elves[::2]
		if is_odd:
			start_pos = 1

print elves[0]
