lines = map(lambda x: x.strip(), open('input.txt').readlines())
connections = {}
unvisited = set()
num_groups = 0

for line in lines:
	first, rest = line.split(' <-> ')
	source = int(first)
	dests = map(int, rest.split(', '))
	connections[source] = dests
	unvisited.add(source)

while(unvisited):
	num_groups += 1
	node = min(unvisited)
	queue = [node]
	visited = set(queue)

	while queue:
		node, queue = queue[0], queue[1:]
		new_nodes = set(connections[node]) - visited
		queue.extend(new_nodes)
		visited.update(new_nodes)
	
	unvisited -= visited

print num_groups