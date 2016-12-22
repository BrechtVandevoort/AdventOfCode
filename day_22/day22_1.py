import re
import itertools

puzzle_input = open('input.txt').readlines()[2:]
nodes = map(lambda x: map(int, re.match('\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)', x).groups()), puzzle_input)

print sum(0 < a[3] <= b[4] for a,b in itertools.permutations(nodes, 2))
