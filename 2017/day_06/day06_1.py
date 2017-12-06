def redistribute(banks):
	index = banks.index(max(banks))
	value = banks[index]
	banks[index] = 0
	while value > 0:
		index = (index + 1) % len(banks)
		banks[index] += 1
		value -= 1
	
banks = map(int, open('input.txt').readline().split())
seen = set()
iterations = 0

while tuple(banks) not in seen:
	seen.add(tuple(banks))
	iterations += 1
	redistribute(banks)
	
print iterations