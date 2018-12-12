def read_input():
    with open("input.txt") as puzzle_input:
        # Initial state
        initial_state = puzzle_input.readline().split()[2]
        
        # Empty line
        puzzle_input.readline()
        
        #
        rules = {}
        for line in puzzle_input:
            parts = line.split()
            rules[parts[0]] = parts[2]
    return initial_state, rules


def shorten_state(first_pot, state):
    first_plant_index = state.find("#")
    last_plant_index = state.rfind("#")
    state = state[first_plant_index:last_plant_index + 1]
    first_pot += first_plant_index
    return first_pot, state


def update_state(first_pot, state, rules):
    #Extend with two empty pots
    state = "...." + state + "...."
    new_state = ""
    first_pot -= 2
    for pos in range(2, len(state) - 2):
        part = state[pos - 2:pos + 3]
        new_state += rules[part]
    first_pot, new_state = shorten_state(first_pot, new_state)
    return first_pot, new_state


state, rules = read_input()
first_pot = 0
# Do first 100 iterations to detect pattern
for i in range(1, 101):
    first_pot, state = update_state(first_pot, state, rules)
    print(i, first_pot, state)

# After 89 generations, a consistent pattern is reached.
# During each iteration, this pattern moves 1 pot to the right.
remaining_iterations = 50000000000 - 100
first_pot += remaining_iterations

s = 0
for pot, plant in zip(range(first_pot, len(state) + first_pot), state):
    if plant == "#":
        s += pot
print("The result is {}.".format(s))