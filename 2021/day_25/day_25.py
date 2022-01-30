from copy import deepcopy

def move_south(fields):
    num_rows = len(fields)
    num_cols = len(fields[0])
    new_fields = deepcopy(fields)
    for r, row in enumerate(fields):
        for c, value in enumerate(row):
            if value == "v" and fields[(r+1)%num_rows][c] == ".":
                new_fields[r][c] = "."
                new_fields[(r+1)%num_rows][c] = "v"
    return new_fields

def move_east(fields):
    num_rows = len(fields)
    num_cols = len(fields[0])
    new_fields = deepcopy(fields)
    for r, row in enumerate(fields):
        for c, value in enumerate(row):
            if value == ">" and fields[r][(c+1)%num_cols] == ".":
                new_fields[r][c] = "."
                new_fields[r][(c+1)%num_cols] = ">"
    return new_fields

def move(fields):
    return move_south(move_east(fields))

def solve_1(data):
    fields = [list(line) for line in data]
    new_fields = move(fields)
    steps = 1
    while fields != new_fields:
        fields = new_fields
        new_fields = move(fields)
        steps += 1
    return steps

def solve_2(data):
    pass

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
