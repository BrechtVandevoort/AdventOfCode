from collections import defaultdict

def get_value(val, registers):
	if val.isalpha():
		return registers[val]
	else:
		return int(val)

def snd(instruction, registers):
	global last_played
	last_played = get_value(instruction[1], registers)
	
def sett(instruction, registers):
	registers[instruction[1]] = get_value(instruction[2], registers)
	
def add(instruction, registers):
	registers[instruction[1]] += get_value(instruction[2], registers)
	
def mul(instruction, registers):
	registers[instruction[1]] *= get_value(instruction[2], registers)

def mod(instruction, registers):
	registers[instruction[1]] %= get_value(instruction[2], registers)
	
def rcv(instruction, registers):
	global last_played
	if get_value(instruction[1], registers) != 0:
		print 'recovered value %d' % (last_played,)

def jgz(instruction, registers):
	global last_played, pointer
	if get_value(instruction[1], registers) > 0:
		pointer += get_value(instruction[2], registers) - 1


instructions = map(lambda x: x.strip().split(), open('input.txt').readlines())
last_played = 0
registers = defaultdict(int)
pointer = 0

instr_map = {
	'snd': snd,
	'set': sett,
	'add': add,
	'mul': mul,
	'mod': mod,
	'rcv': rcv,
	'jgz': jgz
}

while 0 <= pointer < len(instructions):
	instruction = instructions[pointer]
	instr_map[instruction[0]](instruction, registers)
	pointer += 1