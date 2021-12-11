
DIRECTIONS = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1)
}

def move(instr, pos, waypoint_mode=False):
    value = int(instr[1:])
    if instr[0] in DIRECTIONS:
        d = DIRECTIONS[instr[0]]
        if waypoint_mode: # move waypoint
            pos = (pos[0], pos[1], pos[2] + value * d[0], pos[3] + value * d[1])
        else: # move ship
            pos = (pos[0] + value * d[0], pos[1] + value * d[1], pos[2], pos[3])
    elif instr[0] == "F": # move ship towards waypoint/facing
        pos = (pos[0] + value * pos[2], pos[1] + value * pos[3], pos[2], pos[3])
    else: # rotate waypoint/facing
        if instr[0] == "L":
            value = -value
        num_turns = (value % 360) // 90
        for _ in range(num_turns):
            pos = (pos[0], pos[1], pos[3], -pos[2])
    return pos

def solve_1(data):
    pos = (0, 0, 0, 1) # row, col, facing_row, facing_col
    for instr in data:
        pos = move(instr, pos)
    return abs(pos[0]) + abs(pos[1])

def solve_2(data):
    pos = (0, 0, -1, 10) # ship_row, ship_col, waypoint_row, waypoint_col
    for instr in data:
        pos = move(instr, pos, True)
    return abs(pos[0]) + abs(pos[1])

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
