puzzle_input = map(lambda line: line.strip().split('-'), open('input.txt').readlines())
ranges = map(lambda (x,y): (int(x), int(y)), puzzle_input)
ranges = sorted(ranges)

lowest_address = 0
for low, high in ranges:
	if lowest_address >= low:
		lowest_address = max(lowest_address, high+1)
print lowest_address
