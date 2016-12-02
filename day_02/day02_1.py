instructions = map(lambda x: x.strip(), open('input.txt').readlines())
code  = ''
current = 5
for instruction in instructions:
	for move in instruction:
		if move == 'U' and current > 3:
			current -= 3
		if move == 'D' and current < 7:
			current += 3
		if move == 'L' and current % 3 != 1:
			current -= 1
		if move == 'R' and current % 3 > 0:
			current += 1
	code += str(current)
print code
