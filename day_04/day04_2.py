import re

decrypt = lambda c, r: chr(ord('a') + ((ord(c) - ord('a') + r) % 26))

lines = open('input.txt').readlines()
rooms = map(lambda x: re.match('([a-z\-]+)-(\d+)\[([a-z]+)\]', x).groups(), lines)
for room in rooms:
	name, sector, checksum = room
	sector = int(sector)
	name_parts = name.split('-')
	name_chars = ''.join(name_parts)
	counts = {i: name_chars.count(i) for i in set(name_chars)}
	sorted_counts = sorted(counts.iteritems(), cmp=lambda x, y: y[1] - x[1] if x[1] != y[1] else ord(x[0]) - ord(y[0]))
	order = [k for k,v in sorted_counts]
	if checksum == ''.join(order[:5]):
		decrypted_parts = map(lambda part: ''.join(map(lambda c: decrypt(c, sector), part)), name_parts)
		decrypted = ' '.join(decrypted_parts)
		if 'northpole' in decrypted:
			print room, decrypted
