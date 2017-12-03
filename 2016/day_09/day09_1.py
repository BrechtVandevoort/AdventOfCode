import re

data = open('input.txt').read().strip()
output = ''

parts = re.split('\((\d+)x(\d+)\)', data, 1)
while len(parts) > 1:
	output += parts[0]
	c, t = map(int, parts[1:3])
	output += parts[3][:c] * t
	parts = re.split('\((\d+)x(\d+)\)', parts[3][c:], 1)
output += parts[0]

print len(output)
