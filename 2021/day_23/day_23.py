import sys

from numpy import can_cast
sys.setrecursionlimit(10000)

# room positions
R1T = (2, 3)
R1B = (3, 3)
R2T = (2, 5)
R2B = (3, 5)
R3T = (2, 7)
R3B = (3, 7)
R4T = (2, 9)
R4B = (3, 9)
TOP_ROOMS = (R1T, R2T, R3T, R4T)
BOTTOM_ROOMS = (R1B, R2B, R3B, R4B)
ROOMS = TOP_ROOMS

def get_top_room(bottom_room):
    r, c = bottom_room
    return (r-1, c)

def get_bottom_room(top_room):
    r, c = top_room
    return (r+1, c)

DEST_ROOM = {
    "A": R1T,
    "B": R2T,
    "C": R3T,
    "D": R4T
}

DEST_POD = {
    R1T: "A",
    R2T: "B",
    R3T: "C",
    R4T: "D"
}

# hallway positions (where resting is possible)
H1 = (1, 1)
H2 = (1, 2)
H3 = (1, 4)
H4 = (1, 6)
H5 = (1, 8)
H6 = (1, 10)
H7 = (1, 11)
HALLWAYS = (H1, H2, H3, H4, H5, H6, H7)

ALL_LOCATIONS = ROOMS + HALLWAYS

MOVE_COST = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

ROOM_SIZE = 2

def can_move(start, stop, locations):
    # Check for empty hallways
    left_c = min(start[1], stop[1])
    right_c = max(start[1], stop[1])
    for hw in HALLWAYS:
        if left_c <= hw[1] <= right_c and locations[hw] != "" and hw != start:
            return False
    return True

def num_steps(start, stop, locations):
    steps = abs(stop[0] - start[0]) + abs(stop[1] - start[1])
    if start in ROOMS:
        steps += ROOM_SIZE - len(locations[start])
    if stop in ROOMS:
        steps += ROOM_SIZE - 1 - len(locations[stop])
    return steps

def do_move(start, stop, locations):
    new_loc = locations.copy()
    pod = locations[start][0]
    new_loc[start] = new_loc[start][1:]    
    new_loc[stop] = pod + new_loc[stop]
    #print(f"moving {pod} from {start} to {stop}")
    r = find_solution(new_loc)
    if r is not None:
        r += num_steps(start, stop, locations) * MOVE_COST[pod]
    return r

def my_min(v1, v2):
    if v1 is None:
        return v2
    if v2 is None:
        return v1
    return min(v1, v2)

def room_can_accept(room, locations):
    target_pod = DEST_POD[room]
    for c in locations[room]:
        if c != target_pod:
            return False
    return True

#memoization
memo = {}

def find_solution(locations):
    global memo

    # debugging: assert there are still the same number of pods
    counter = sum(len(pod) for pod in locations.values())
    assert(counter == ROOM_SIZE * 4)

    # check for solution state
    is_solution = True
    for room in ROOMS:
        if not room_can_accept(room, locations):
            is_solution = False
            break
    for hw in HALLWAYS:
        if locations[hw] != "":
            is_solution = False
            break
    if is_solution:
        return 0

    if repr(locations) in memo:
        return memo[repr(locations)]
    best = None
    for room in ROOMS:
        #if room in accepting state, we no longer move pods out of the room
        if room_can_accept(room, locations):
            continue
        # try moving into the hallway
        for hw in HALLWAYS:
            if can_move(room, hw, locations):
                r = do_move(room, hw, locations)
                best = my_min(best, r)

    for hw in HALLWAYS:
        pod = locations[hw]
        if pod == "":
            continue
        dest_room = DEST_ROOM[pod]
        if room_can_accept(dest_room, locations) and can_move(hw, dest_room, locations):
            r = do_move(hw, dest_room, locations)
            best = my_min(best, r)
    memo[repr(locations)] = best
    return best

def parse_data(data):
    r1 = data[2]
    r2 = data[3]
    locations = {l: "" for l in ALL_LOCATIONS}
    for r, c in TOP_ROOMS:
        locations[(r, c)] += data[r][c]
    for r, c in BOTTOM_ROOMS:
        locations[(r-1, c)] += data[r][c]
    return locations

def solve_1(data):
    locations = parse_data(data)
    best_cost = find_solution(locations)
    return best_cost

def solve_2(data):
    global ROOM_SIZE
    ROOM_SIZE = 4
    locations = parse_data(data)
    locations[R1T] = locations[R1T][0] + "DD" + locations[R1T][1]
    locations[R2T] = locations[R2T][0] + "CB" + locations[R2T][1]
    locations[R3T] = locations[R3T][0] + "BA" + locations[R3T][1]
    locations[R4T] = locations[R4T][0] + "AC" + locations[R4T][1]
    best_cost = find_solution(locations)
    return best_cost

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip("\n"), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
