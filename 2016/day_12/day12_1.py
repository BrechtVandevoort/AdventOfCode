import re
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

instructions = open('input.txt').readlines()
instruction_pointer = 0

while 0 <= instruction_pointer < len(instructions):
	parts = instructions[instruction_pointer].split()
	if parts[0] == 'cpy':
		registers[parts[2]] = registers[parts[1]] if parts[1] in registers else int(parts[1])
	elif parts[0] == 'inc':
		registers[parts[1]] += 1
	elif parts[0] == 'dec':
		registers[parts[1]] -= 1
	elif parts[0] == 'jnz':
		x = registers[parts[1]] if parts[1] in registers else int(parts[1])
		y = registers[parts[2]] if parts[2] in registers else int(parts[2])
		if x:
			instruction_pointer += y - 1
	instruction_pointer += 1

print registers['a']
