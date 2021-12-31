def parse_data(data):
    return list(map(lambda x: list(map(int, x)), data))

def do_step(field):
    num_rows = len(field)
    num_cols = len(field[0])
    will_flash = []
    for r in range(num_rows):
        for c in range(num_cols):
            field[r][c] += 1
            if field[r][c] == 10:
                will_flash.append((r, c))
    i = 0
    while i < len(will_flash):
        r, c = will_flash[i]
        for x in range(max(0, r-1), min(num_rows, r+2)):
            for y in range(max(0, c-1), min(num_cols, c+2)):
                field[x][y] += 1
                if field[x][y] == 10:
                    will_flash.append((x, y))
        i += 1
    for r, c in will_flash:
        field[r][c] = 0
    return len(will_flash)

def solve_1(data):
    field = parse_data(data)
    return sum(do_step(field) for _ in range(100))

def solve_2(data):
    field = parse_data(data)
    size = len(field) * len(field[0])
    step = 0
    num_flash = 0
    while num_flash != size:
        step += 1
        num_flash = do_step(field)
    return step

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
