instructions = map(int, open('input.txt'))
pointer = 0
steps = 0

while 0 <= pointer < len(instructions):
	steps += 1
	prevpointer = pointer
	pointer += instructions[pointer]
	if instructions[prevpointer] >= 3:
		instructions[prevpointer] -= 1
	else:
		instructions[prevpointer] += 1

print steps
