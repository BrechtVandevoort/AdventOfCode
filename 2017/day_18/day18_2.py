from collections import defaultdict

def get_value(val, registers):
	if val.isalpha():
		return registers[val]
	else:
		return int(val)

def snd(instruction, prog, other):
	global counter
	if prog['pid'] == 1:
		counter += 1
	registers = prog['registers']
	other_queue = other['queue']
	other_queue.append(get_value(instruction[1], registers))
	
def sett(instruction, prog, other):
	registers = prog['registers']
	registers[instruction[1]] = get_value(instruction[2], registers)
	
def add(instruction, prog, other):
	registers = prog['registers']
	registers[instruction[1]] += get_value(instruction[2], registers)
	
def mul(instruction, prog, other):
	registers = prog['registers']
	registers[instruction[1]] *= get_value(instruction[2], registers)

def mod(instruction, prog, other):
	registers = prog['registers']
	registers[instruction[1]] %= get_value(instruction[2], registers)
	
def rcv(instruction, prog, other):
	registers = prog['registers']
	queue = prog['queue']
	registers[instruction[1]] = queue.pop(0)

def jgz(instruction, prog, other):
	registers = prog['registers']
	if get_value(instruction[1], registers) > 0:
		prog['pointer'] += get_value(instruction[2], registers) - 1


instructions = map(lambda x: x.strip().split(), open('input.txt').readlines())
counter = 0
program_0 = {
	'pid': 0,
	'registers': defaultdict(int),
	'pointer': 0,
	'queue': []
}
program_1 = {
	'pid': 1,
	'registers': defaultdict(int),
	'pointer': 0,
	'queue': []
}
program_1['registers']['p'] = 1

instr_map = {
	'snd': snd,
	'set': sett,
	'add': add,
	'mul': mul,
	'mod': mod,
	'rcv': rcv,
	'jgz': jgz
}

prog, other = program_0, program_1
stopped = False

while not stopped:
	stopped = True
	while 0 <= prog['pointer'] < len(instructions):
		instruction = instructions[prog['pointer']]
		if instruction[0] == 'rcv' and len(prog['queue']) == 0:
			break
		instr_map[instruction[0]](instruction, prog, other)
		prog['pointer'] += 1
		stopped = False
	prog, other = other, prog

print counter