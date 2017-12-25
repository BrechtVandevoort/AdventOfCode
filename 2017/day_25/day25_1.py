import re
from collections import defaultdict

info_pattern = '''Begin in state ([A-Z]).
Perform a diagnostic checksum after (\d+) steps.'''

transition_pattern = '''In state ([A-Z]):
  If the current value is ([01]):
    - Write the value ([01]).
    - Move one slot to the (\w+).
    - Continue with state ([A-Z]).
  If the current value is ([01]):
    - Write the value ([01]).
    - Move one slot to the (\w+).
    - Continue with state ([A-Z]).'''

direction_map = {
	'left': -1,
	'right': 1
}

puzzle_input = open('input.txt').read()
transition_parsed = re.findall(transition_pattern, puzzle_input)
info_parsed = re.findall(info_pattern, puzzle_input)[0]
transitions = {}
current_state = info_parsed[0]
num_steps = int(info_parsed[1])
tape = defaultdict(int)
cursor = 0

for match in transition_parsed:
	state = match[0]
	val_0 = int(match[1])
	val_1 = int(match[5])
	write_0 = int(match[2])
	write_1 = int(match[6])
	dir_0 = direction_map[match[3]]
	dir_1 = direction_map[match[7]]
	transitions[(state, val_0)] = (write_0, dir_0, match[4])
	transitions[(state, val_1)] = (write_1, dir_1, match[8])

for _ in xrange(num_steps):
	val = tape[cursor]
	instruction = transitions[(current_state, val)]
	tape[cursor] = instruction[0]
	cursor += instruction[1]
	current_state = instruction[2]

print sum(tape.values())