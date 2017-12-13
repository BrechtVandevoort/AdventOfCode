lines = map(lambda x: x.strip().split(': '), open('input.txt').readlines())
layers = {int(line[0]) : int(line[1]) for line in lines}
max_depth = max(layers)
severity = 0

for step in xrange(max_depth+1):
	if step in layers:
		area = layers[step]
		if step % ((area - 1) * 2) == 0:
			severity += step * area

print severity