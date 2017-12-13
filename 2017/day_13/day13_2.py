lines = map(lambda x: x.strip().split(': '), open('input.txt').readlines())
layers = {int(line[0]) : int(line[1]) for line in lines}
max_depth = max(layers)
caught = True
delay = 0

while caught:
	delay += 1
	caught = False
	for stp in xrange(max_depth+1):
		step = delay + stp
		if stp in layers:
			area = layers[stp]
			if step % ((area - 1) * 2) == 0:
				caught = True
				break
	
print delay