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
for i in range(20):
    first_pot, state = update_state(first_pot, state, rules)

s = 0
for pot, plant in zip(range(first_pot, len(state) + first_pot), state):
    if plant == "#":
        s += pot
print("The result is {}.".format(s))