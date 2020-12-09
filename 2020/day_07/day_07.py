import re

def parse_line(line):
    """
    >>> parse_line("wavy coral bags contain 4 pale purple bags, 2 bright olive bags.")
    ("wavy coral", [(4, "pale purple"), (2, "bright olive")])
    """
    bag_type = " ".join(line.split(" ")[:2])
    contains = re.findall(r"(\d+) (\w+ \w+)", line)
    contains = list(map(lambda x: (int(x[0]), x[1]), contains))
    return bag_type, contains

def invert_containment(containment):
    contained_in = {bag: [] for bag in containment}
    for bag, contains in containment.items():
        for c in contains:
            contained_in[c[1]].append(bag)
    return contained_in

def required_bags(containment, bag):
    required = 1 # the bag itself
    for num_required, bag_type in containment[bag]:
        required += num_required * required_bags(containment, bag_type)
    return required

def solve_1(data):
    containment = dict(map(parse_line, data))
    contained_in = invert_containment(containment)
    other_bags = []
    frontier = ["shiny gold"]
    while len(frontier) > 0:
        bag = frontier.pop(0)
        for other_bag in contained_in[bag]:
            if other_bag not in other_bags:
                other_bags.append(other_bag)
                frontier.append(other_bag)
    return len(other_bags)

def solve_2(data):
    containment = dict(map(parse_line, data))
    return required_bags(containment, "shiny gold") - 1 #not counting the shiny bag itself

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
