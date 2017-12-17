puzzle_input = 328
buff = [0]
pos = 0

for i in xrange(1, 2018):
	pos = (pos + puzzle_input + 1) % len(buff)
	buff.insert(pos, i)
	
print buff[pos+1]