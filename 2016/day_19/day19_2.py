puzzle_input = 3014387
elves = [i for i in xrange(1, puzzle_input + 1)]

pos = 0
while len(elves) > 1:
	l = len(elves)
	if l % 1000 == 0:
		print l
	target = (pos + l / 2) % l
	#print elves[pos], 'killed', elves[target]
	del elves[target]
	if target > pos:
		pos = (pos + 1)
	pos %= len(elves)

print elves[0]
