puzzle_input = open('input.txt').readlines()
puzzle_input_word = 'abcdefgh'

instructions = [line.strip().split() for line in puzzle_input]
scramble = list(puzzle_input_word)

for instruction in instructions:
	if instruction[0] == 'swap':
		if instruction[1] == 'position':
			x, y = int(instruction[2]), int(instruction[5])
			scramble[x], scramble[y] = scramble[y], scramble[x]
		if instruction[1] == 'letter':
			a,b = instruction[2], instruction[5]
			x,y = scramble.index(a), scramble.index(b)
			scramble[x], scramble[y] = scramble[y], scramble[x]
	if instruction[0] == 'rotate':
		if instruction[1] == 'left':
			rotation = int(instruction[2]) % len(scramble)
		elif instruction[1] == 'right':
			rotation = (len(scramble) - int(instruction[2])) % len(scramble)
		else:
			x = scramble.index(instruction[6])
			rotation = x + 1 if x < 4 else x + 2
			rotation = (len(scramble) - rotation) % len(scramble)
		scramble = scramble[rotation:] + scramble[:rotation]
	if instruction[0] == 'reverse':
		x, y = int(instruction[2]), int(instruction[4])+1
		scramble = scramble[:x] + list(reversed(scramble[x:y])) + scramble[y:]
	if instruction[0] == 'move':
		x,y = int(instruction[2]), int(instruction[5])
		a = scramble.pop(x)
		scramble.insert(y, a)

print ''.join(scramble)
