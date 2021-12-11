
def in_bounds(seats, row, col):
    return 0 <= row < len(seats) and 0 <= col < len(seats[row])

def adjacent_seats_immediate(seats, row, col):
    adj = ""
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if (r != row or c != col) and in_bounds(seats, r, c):
                adj += seats[r][c]
    return adj

def adjacent_seats_first(seats, row, col):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    adj = ""
    for d in directions:
        r = row + d[0]
        c = col + d[1]
        while in_bounds(seats, r, c) and seats[r][c] == ".":
            r += d[0]
            c += d[1]
        if in_bounds(seats, r, c):
            adj += seats[r][c]
    return adj

def predict_seat(seats, row, col, adj_func, tolerance):
    seat = seats[row][col]
    if seat != ".":
        occupied = adj_func(seats, row, col).count("#")
        if seat == "L" and occupied == 0:
            return "#"
        if seat == "#" and occupied >= tolerance:
            return "L"
    return seat

def iteration(seats, adj_func, tolerance):
    new_seats = []
    for i, row in enumerate(seats):
        new_row = ""
        for j in range(len(row)):
            new_row += predict_seat(seats, i, j, adj_func, tolerance)
        new_seats.append(new_row)
    return new_seats

def solve(seats, adj_func, tolerance):
    old_state = seats
    new_state = iteration(old_state, adj_func, tolerance)
    while old_state != new_state:
        old_state = new_state
        new_state = iteration(old_state, adj_func, tolerance)
    return sum(map(lambda s: s.count("#"), new_state))

def solve_1(data):
    return solve(data, adjacent_seats_immediate, 4)

def solve_2(data):
    return solve(data, adjacent_seats_first, 5)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
