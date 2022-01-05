def parse_data(data):
    return list(map(lambda x: list(map(int, x)), data))

def find_best_path(field):
    num_rows = len(field)
    num_cols = len(field[0])
    min_risk = [[None for _ in row] for row in field]
    min_risk[0][0] = 0
    queue = [(0,0)]
    while queue:
        row, col = queue.pop(0)
        rc_risk = min_risk[row][col]
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = row+dr, col+dc
            if 0 <= nr < num_rows and 0 <= nc < num_cols:
                if min_risk[nr][nc] is None or rc_risk + field[nr][nc] < min_risk[nr][nc]:
                    min_risk[nr][nc] = rc_risk + field[nr][nc]
                    queue.append((nr, nc))
    return min_risk[-1][-1]

def solve_1(data):
    field = parse_data(data)
    return find_best_path(field)

def solve_2(data):
    small_field = parse_data(data)
    # extend each row
    for row in small_field:
        values = row[:]
        for i in range(1, 5):
            new_values = [(v + i) % 9 if v + i >= 10 else v + i for v in values]
            row.extend(new_values)
    field = small_field[:]
    # extend number of rows
    for i in range(1, 5):
        for row in small_field:
            new_row = [(v + i) % 9 if v + i >= 10 else v + i for v in row]
            field.append(new_row)

    return find_best_path(field)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
