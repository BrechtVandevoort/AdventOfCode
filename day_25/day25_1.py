instructions = list(map(lambda x: list(x.split()), open('input.txt').readlines()))

def execute_assembunny(register_a):
	registers = {'a': register_a, 'b': 0, 'c': 0, 'd': 0}
	instruction_pointer = 0

	while 0 <= instruction_pointer < len(instructions):
		parts = instructions[instruction_pointer]
		if parts[0] == 'cpy' and len(parts) == 3:
			registers[parts[2]] = registers[parts[1]] if parts[1] in registers else int(parts[1])
		elif parts[0] == 'inc' and len(parts) == 2:
			registers[parts[1]] += 1
		elif parts[0] == 'dec' and len(parts) == 2:
			registers[parts[1]] -= 1
		elif parts[0] == 'jnz' and len(parts) == 3:
			x = registers[parts[1]] if parts[1] in registers else int(parts[1])
			y = registers[parts[2]] if parts[2] in registers else int(parts[2])
			if x:
				instruction_pointer += y - 1
		elif parts[0] == 'out':
			x = registers[parts[1]] if parts[1] in registers else int(parts[1])
			yield x
		elif parts[0] == 'tgl' and len(parts) == 2:
			x = registers[parts[1]] if parts[1] in registers else int(parts[1])
			if 0 <= instruction_pointer + x < len(instructions):
				target = instructions[instruction_pointer + x]
				if len(target) == 2:
					target[0] = 'dec' if target[0] == 'inc' else 'inc'
				if len(target) == 3:
					target[0] = 'cpy' if target[0] == 'jnz' else 'jnz'
		else:
			print 'invalid instruction:', parts
		instruction_pointer += 1

for a in range(10000):
	correct = True
	count = 0
	generator = execute_assembunny(a)
	while correct and count < 20:
		if count % 2 != generator.next():
			correct = False
		count += 1
	if correct:
		print a
