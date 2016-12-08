import re

operations = [re.match('(?:rotate )?([a-z]+) (?:[xy]=)?([0-9]+)(?:x| by )([0-9]+)', line).groups() for line in open('input.txt').readlines()]
screen = [[' ' for _ in range(50)] for _ in range(6)]

for operation in operations:
	op, a, b = operation[0], int(operation[1]), int(operation[2])
	if op == 'rect':
		for row in range(b):
			for col in range(a):
				screen[row][col] = '#'
	elif op == 'row':
		old_row = [screen[a][i] for i in range(50)]
		for i in range(50):
			screen[a][i] = old_row[(i - b)%50]
	elif op == 'column':
		old_col = [screen[i][a] for i in range(6)]
		for i in range(6):
			screen[i][a] = old_col[(i - b)%6]

print sum( 1 for row in range(6) for col in range(50) if screen[row][col] == '#')

for line in screen:
	print ''.join(line)
