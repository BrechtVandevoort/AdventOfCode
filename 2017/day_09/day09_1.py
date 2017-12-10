stream = open('input.txt').readline().strip()
score = 0
depth = 0
garbage_flag = False
ignore_flag = False

for c in stream:
	if garbage_flag:
		if ignore_flag:
			ignore_flag = False
		else:
			if c == '!':
				ignore_flag = True
			elif c == '>':
				garbage_flag = False
	else:
		if c == '{':
			depth += 1
		elif c == '}':
			score += depth
			depth -= 1
		elif c == '<':
			garbage_flag = True

print score