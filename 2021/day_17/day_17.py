import re

def parse_data(data):
    return list(map(int, re.findall("-?\d+", data[0])))

def test_trajectory(dx, dy, min_x, max_x, min_y, max_y):
    pos = (0, 0)
    while pos[1] >= min_y and pos[0] <= max_x and (dx > 0 or min_x <= pos[0]):
        pos = pos[0] + dx, pos[1] + dy
        dx = max(0, dx - 1)
        dy -= 1
        if min_x <= pos[0] <= max_x and min_y <= pos[1] <= max_y:
            return True
    return False

def heighest_point(dy):
    pos = 0
    while dy > 0:
        pos += dy
        dy -= 1
    return pos


def solve_1(data):
    min_x, max_x, min_y, max_y = parse_data(data)
    max_height = 0
    for y in range(500):
        for x in range(max_x+1):
            if test_trajectory(x, y, min_x, max_x, min_y, max_y):
                max_height = max(max_height, heighest_point(y))
    return max_height


def solve_2(data):
    min_x, max_x, min_y, max_y = parse_data(data)
    num_ok = 0
    for y in range(min_y, 500):
        for x in range(max_x+1):
            if test_trajectory(x, y, min_x, max_x, min_y, max_y):
                num_ok += 1
    return num_ok

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
