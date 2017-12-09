from collections import defaultdict

instructions = map(lambda x: x.strip(), open('input.txt').readlines())
registers = defaultdict(int)
operations = {
	'inc': lambda x, y: x + y,
	'dec': lambda x, y: x - y
}
cond_operations = {
	'<': lambda x, y: x < y,
	'>': lambda x, y: x > y,
	'<=': lambda x, y: x <= y,
	'>=': lambda x, y: x >= y,
	'==': lambda x, y: x == y,
	'!=': lambda x, y: x != y,
}

for instruction in instructions:
	reg, op, val, _, cond_reg, cond_op, cond_val = instruction.split()
	val = int(val)
	cond_val = int(cond_val)
	if cond_operations[cond_op](registers[cond_reg], cond_val):
		registers[reg] = operations[op](registers[reg], val)
		
print max(registers.values())