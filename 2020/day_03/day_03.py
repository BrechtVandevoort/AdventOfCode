import math

def go_down_slope(data, slope_rows, slope_cols):
    row = 0
    col = 0
    num_trees = 0
    while row < len(data):
        if data[row][col] == "#":
            num_trees += 1
        row += slope_rows
        col = (col + slope_cols) % len(data[0])
    return num_trees

def solve_1(data):
    return go_down_slope(data, 1, 3)

def solve_2(data):
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    return math.prod(go_down_slope(data, r, c) for r, c in slopes)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
