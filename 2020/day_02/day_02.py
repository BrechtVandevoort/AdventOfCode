import re

def parse_data(data):
    pattern = re.compile("(\d+)-(\d+) (\w): (\w+)")
    result = [re.match(pattern, s).groups() for s in data]
    return result

def solve_1(data):
    parsed_data = parse_data(data)
    num_valid = 0
    for mn, mx, c, pw in parsed_data:
        if int(mn) <= pw.count(c) <= int(mx):
            num_valid += 1
    return num_valid

def solve_2(data):
    parsed_data = parse_data(data)
    num_valid = 0
    for p1, p2, c, pw in parsed_data:
        if (pw[int(p1)-1] == c) != (pw[int(p2)-1] == c):
            num_valid += 1
    return num_valid

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
