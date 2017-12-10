stream = open('input.txt').readline().strip()
depth = 0
size = 0
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
				size += 1
	else:
		if c == '<':
			garbage_flag = True

print size