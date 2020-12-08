
def bin_search(repr, min_id, max_id):
    if len(repr) == 0:
        return min_id
    half_dist = (max_id - min_id + 1) // 2
    if repr[0] == "0":
        return bin_search(repr[1:], min_id, max_id - half_dist)
    return bin_search(repr[1:], min_id + half_dist, max_id)

def seat_id(seat_repr):
    row_repr = seat_repr[:7].replace("F", "0").replace("B", "1")
    col_repr = seat_repr[7:].replace("L", "0").replace("R", "1")
    row_id = bin_search(row_repr, 0, 127)
    col_id = bin_search(col_repr, 0, 8)
    return row_id * 8 + col_id

def solve_1(data):
    return max(seat_id(seat_repr) for seat_repr in data)

def solve_2(data):
    occupied = sorted(seat_id(seat_repr) for seat_repr in data)
    for i, val in enumerate(occupied[:-1]):
        if val + 2 == occupied[i+1]:
            return val + 1

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
