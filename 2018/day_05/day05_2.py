import string

def is_opposite(a, b):
    return a != b and a.lower() == b.lower()


def react_polymer(polymer):
    i = 0
    while i < len(polymer) - 1:
        if is_opposite(polymer[i], polymer[i+1]):
            polymer = polymer[:i] + polymer[i+2:]
            i = max(0, i - 1)
        else:
            i += 1
    return polymer

with open("input.txt") as puzzle_input:
    polymer = puzzle_input.read().strip()

min_size = None
for c in string.ascii_uppercase:
    new_polymer = polymer.replace(c, "")
    new_polymer = new_polymer.replace(c.lower(), "")
    resulting_polymer = react_polymer(new_polymer)
    if min_size is None or min_size > len(resulting_polymer):
        min_size = len(resulting_polymer)

print("The best result has length {}.".format(min_size))