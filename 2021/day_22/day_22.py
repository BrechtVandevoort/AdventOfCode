from collections import defaultdict
import re

xmin = 0
xmax = 1
ymin = 2
ymax = 3
zmin = 4
zmax = 5

def parse_data(data):
    instructions = []
    for line in data:
        tp = 1 if line[1] == "n" else 0
        coords = re.findall("-?\d+", line)
        coords = tuple(map(int, coords))
        instructions.append((tp, coords))
    return instructions

def interl_1d(c1, c2):
    return (c1[1] >= c2[0]) and (c2[1] >= c1[0])

def interleaving(c1, c2):
    return interl_1d((c1[0], c1[1]), (c2[0], c2[1])) and\
            interl_1d((c1[2], c1[3]), (c2[2], c2[3])) and\
            interl_1d((c1[4], c1[5]), (c2[4], c2[5]))

def set_off(are_on, c1):
    for c2 in are_on.copy():
        if not interleaving(c1, c2):
            continue
        # remove c2 from are_on
        are_on.remove(c2)
        # add everthing before c1[xmin]
        if c2[xmin] < c1[xmin]:
            are_on.add((c2[xmin], c1[xmin]-1, c2[ymin], c2[ymax], c2[zmin], c2[zmax]))
        # add everthing after c1[xmax]
        if c2[xmax] > c1[xmax]:
            are_on.add((c1[xmax]+1, c2[xmax], c2[ymin], c2[ymax], c2[zmin], c2[zmax]))
        min_x = max(c1[xmin], c2[xmin])
        max_x = min(c1[xmax], c2[xmax])
        # add everthing before c1[ymin]
        if c2[ymin] < c1[ymin]:
            are_on.add((min_x, max_x, c2[ymin], c1[ymin]-1, c2[zmin], c2[zmax]))
        # add everthing after c1[ymax]
        if c2[ymax] > c1[ymax]:
            are_on.add((min_x, max_x, c1[ymax]+1, c2[ymax], c2[zmin], c2[zmax]))
        min_y = max(c1[ymin], c2[ymin])
        max_y = min(c1[ymax], c2[ymax])
        # add everthing before c1[zmin]
        if c2[zmin] < c1[zmin]:
            are_on.add((min_x, max_x, min_y, max_y, c2[zmin], c1[zmin]-1))
        # add everthing after c1[zmax]
        if c2[zmax] > c1[zmax]:
            are_on.add((min_x, max_x, min_y, max_y, c1[zmax]+1, c2[zmax]))
        

def solve_1(data):
    return solve_2(data[:20])
    # instructions = parse_data(data)
    # cells = defaultdict(int)
    # for i, (tp, coords) in enumerate(instructions[:20]):
    #     #print(f"instruction {i+1} of {len(instructions)}")
    #     for x in range(coords[0], coords[1]+1):
    #         for y in range(coords[2], coords[3]+1):
    #             for z in range(coords[4], coords[5]+1):
    #                 cells[(x,y,z)] = tp
    # return sum(cells.values())

def solve_2(data):
    instructions = parse_data(data)
    are_on = set()
    for i, (tp, coords) in enumerate(instructions[:]):
        #print(f"instruction {i+1} of {len(instructions)}")
        set_off(are_on, coords)
        if tp == 1:
            are_on.add(coords)
    s = 0
    for coords in are_on:
        s += (coords[1] - coords[0] + 1) * (coords[3] - coords[2] + 1) * (coords[5] - coords[4] + 1)
    return s

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
