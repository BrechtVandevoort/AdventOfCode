import re

lines = open('input.txt').readlines()
rooms = map(lambda x: re.match('([a-z\-]+)-(\d+)\[([a-z]+)\]', x).groups(), lines)
rooms = map(lambda (name, sector, checksum): (''.join(name.split('-')), int(sector), checksum), rooms)
sector_sum = 0
for room in rooms:
	name, sector, checksum = room
	counts = {i: name.count(i) for i in set(name)}
	sorted_counts = sorted(counts.iteritems(), cmp=lambda x, y: y[1] - x[1] if x[1] != y[1] else ord(x[0]) - ord(y[0]))
	order = [k for k,v in sorted_counts]
	if checksum == ''.join(order[:5]):
		sector_sum += sector
print sector_sum
