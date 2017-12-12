lines = map(lambda x: x.strip(), open('input.txt').readlines())
connections = {}
queue = [0]
visited = set([0])

for line in lines:
	source, rest = line.split(' <-> ')
	dests = map(int, rest.split(', '))
	connections[int(source)] = dests

while queue:
	node, queue = queue[0], queue[1:]
	new_nodes = set(connections[node]) - visited
	queue.extend(new_nodes)
	visited.update(new_nodes)

print len(visited)