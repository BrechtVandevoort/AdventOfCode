registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}

instructions = list(map(lambda x: list(x.split()), open('improved_input.txt').readlines()))
instruction_pointer = 0

while 0 <= instruction_pointer < len(instructions):
	parts = instructions[instruction_pointer]
	if parts[0] == 'cpy' and len(parts) == 3:
		registers[parts[2]] = registers[parts[1]] if parts[1] in registers else int(parts[1])
	elif parts[0] == 'mul' and len(parts) == 4:
		x = registers[parts[1]] if parts[1] in registers else int(parts[1])
		y = registers[parts[2]] if parts[2] in registers else int(parts[2])
		registers[parts[3]] = x*y
	elif parts[0] == 'inc' and len(parts) == 2:
		registers[parts[1]] += 1
	elif parts[0] == 'dec' and len(parts) == 2:
		registers[parts[1]] -= 1
	elif parts[0] == 'jnz' and len(parts) == 3:
		x = registers[parts[1]] if parts[1] in registers else int(parts[1])
		y = registers[parts[2]] if parts[2] in registers else int(parts[2])
		if x:
			instruction_pointer += y - 1
	elif parts[0] == 'tgl' and len(parts) == 2:
		x = registers[parts[1]] if parts[1] in registers else int(parts[1])
		if 0 <= instruction_pointer + x < len(instructions):
			target = instructions[instruction_pointer + x]
			if len(target) == 2:
				target[0] = 'dec' if target[0] == 'inc' else 'inc'
			if len(target) == 3:
				target[0] = 'cpy' if target[0] == 'jnz' else 'jnz'
	elif parts[0] == 'pass':
		pass
	else:
		print 'invalid instruction:', parts
	instruction_pointer += 1

print registers['a']
