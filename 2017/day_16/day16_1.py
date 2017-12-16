instructions = open('input.txt').read().strip().split(',')
order = list('abcdefghijklmnop')

for instr in instructions:
	if instr[0] == 's':
		num = int(instr[1:])
		order = order[-num:] + order[:-num]
	else:
		num1, num2 = 0, 0
		if instr[0] == 'x':
			num1, num2 = map(int, instr[1:].split('/'))
		elif instr[0] == 'p':
			c1, c2 = instr[1:].split('/')
			num1 = order.index(c1)
			num2 = order.index(c2)
		order[num1], order[num2] = order[num2], order[num1]
	
print ''.join(order)
