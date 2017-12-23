from collections import defaultdict

def get_value(val, registers):
	if val.isalpha():
		return registers[val]
	else:
		return int(val)

def sett(instruction, registers):
	registers[instruction[1]] = get_value(instruction[2], registers)
	
def sub(instruction, registers):
	registers[instruction[1]] -= get_value(instruction[2], registers)
	
def mul(instruction, registers):
	registers[instruction[1]] *= get_value(instruction[2], registers)

def jnz(instruction, registers):
	global last_played, pointer
	if get_value(instruction[1], registers) != 0:
		pointer += get_value(instruction[2], registers) - 1


instructions = map(lambda x: x.strip().split(), open('input.txt').readlines())
num_mul = 0
registers = defaultdict(int)
pointer = 0

instr_map = {
	'set': sett,
	'sub': sub,
	'mul': mul,
	'jnz': jnz
}

while 0 <= pointer < len(instructions):
	instruction = instructions[pointer]
	if instruction[0] == 'mul':
		num_mul += 1
	instr_map[instruction[0]](instruction, registers)
	pointer += 1
	
print num_mul