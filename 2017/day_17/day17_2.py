puzzle_input = 328
pos = 0
result = 0

for i in xrange(1, 50000001):
	pos = (pos + puzzle_input + 1) % i
	if pos == 0:
		result = i
	
print result