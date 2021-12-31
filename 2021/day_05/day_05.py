import re
from typing import DefaultDict

def parse_data(data):
    result = []
    for line in data:
        nums = map(int, re.findall("\d+", line))
        result.append(list(nums))
    return result

def solve(data, ignore_diagonal):
    lines = parse_data(data)
    field = DefaultDict(int)
    for x1,y1,x2,y2 in lines:
        x_diff = x2 - x1
        if x_diff != 0:
            x_diff //= abs(x_diff)
        y_diff = y2 - y1
        if y_diff != 0:
            y_diff //= abs(y_diff)
        if x_diff == 0 or y_diff == 0 or not ignore_diagonal:
            x, y = x1, y1
            field[(x,y)] += 1
            while x != x2 or y != y2:
                x += x_diff
                y += y_diff
                field[(x,y)] += 1                
    return sum(1 for v in field.values() if v >= 2)

def solve_1(data):
    return solve(data, True)

def solve_2(data):
    return solve(data, False)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
