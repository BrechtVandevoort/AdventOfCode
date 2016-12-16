puzzle_input = '01110110101001000'
disk_size = 272

data = puzzle_input
while len(data) < disk_size:
	data += '0' + ''.join('0' if x == '1' else '1' for x in reversed(data))

data = data[:disk_size]
while len(data) % 2 == 0:
	data = ''.join('1' if data[i] == data[i+1] else '0' for i in xrange(0,len(data), 2))
print data
