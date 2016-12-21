def rotate_based_on(scramble, target):
	x = scramble.index(target)
	rotation = x + 1 if x < 4 else x + 2
	rotation = (len(scramble) - rotation) % len(scramble)
	scramble = scramble[rotation:] + scramble[:rotation]
	return scramble

def reverse_rotate_based_on(scramble, target):
	unscramble = scramble[:]
	while scramble != rotate_based_on(unscramble, target):
		unscramble = unscramble[1:] + unscramble[:1]
	return unscramble

puzzle_input = open('input.txt').readlines()
puzzle_input_word = 'fbgdceah'

instructions = [line.strip().split() for line in puzzle_input]
scramble = list(puzzle_input_word)

for instruction in reversed(instructions):
	if instruction[0] == 'swap':
		if instruction[1] == 'position':
			x, y = int(instruction[2]), int(instruction[5])
			scramble[x], scramble[y] = scramble[y], scramble[x]
		if instruction[1] == 'letter':
			a,b = instruction[2], instruction[5]
			x,y = scramble.index(a), scramble.index(b)
			scramble[x], scramble[y] = scramble[y], scramble[x]
	if instruction[0] == 'rotate':
		if instruction[1] == 'right':
			rotation = int(instruction[2]) % len(scramble)
			scramble = scramble[rotation:] + scramble[:rotation]
		elif instruction[1] == 'left':
			rotation = (len(scramble) - int(instruction[2])) % len(scramble)
			scramble = scramble[rotation:] + scramble[:rotation]
		else:
			scramble = reverse_rotate_based_on(scramble, instruction[6])
	if instruction[0] == 'reverse':
		x, y = int(instruction[2]), int(instruction[4])+1
		scramble = scramble[:x] + list(reversed(scramble[x:y])) + scramble[y:]
	if instruction[0] == 'move':
		y,x = int(instruction[2]), int(instruction[5])
		a = scramble.pop(x)
		scramble.insert(y, a)

print ''.join(scramble)
