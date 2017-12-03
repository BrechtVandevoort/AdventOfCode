import re

discs = [map(int, re.match('Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)', line).groups()) for line in open('input.txt').readlines()]

i = 0
while True:
	for disc in discs:
		flag = True
		if 0 != (disc[0] + disc[2] + i) % disc[1]:
			flag = False
			break
	if flag:
		print i
		break
	i += 1
