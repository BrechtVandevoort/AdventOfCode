instructions = map(lambda x: x.strip(), open('input.txt').readlines())

keypad = [
	'       ',
	'   1   ',
	'  234  ',
	' 56789 ',
	'  ABC  ',
	'   D   ',
	'       '
]

code  = ''
current = [3, 1]
for instruction in instructions:
	for move in instruction:
		if move == 'U' and keypad[current[0]-1][current[1]] != ' ':
			current[0] -= 1
		if move == 'D' and keypad[current[0]+1][current[1]] != ' ':
			current[0] += 1
		if move == 'L' and keypad[current[0]][current[1]-1] != ' ':
			current[1] -= 1
		if move == 'R' and keypad[current[0]][current[1]+1] != ' ':
			current[1] += 1
	code += keypad[current[0]][current[1]]
print code
