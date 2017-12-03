import re

def decompressed_length(data):
	length = 0
	parts = re.split('\((\d+)x(\d+)\)', data, 1)
	while len(parts) > 1:
		length += len(parts[0])
		c, t = map(int, parts[1:3])
		length += decompressed_length(parts[3][:c]) * t
		parts = re.split('\((\d+)x(\d+)\)', parts[3][c:], 1)
	length += len(parts[0])
	return length

data = open('input.txt').read().strip()
print decompressed_length(data)
