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

resulting_polymer = react_polymer(polymer)

print("The remaining polymer has length {}.".format(len(resulting_polymer)))
