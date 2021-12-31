
def parse_data(data):
    heights = list(map(lambda x: [9] + list(map(int, x)) + [9], data))
    padding = [9 for _ in range(len(heights[0]))]
    return [padding] + heights + [padding[:]]

def all_deepest(heights):
    coord_list = []
    for r in range(1, len(heights)-1):
        for c in range(1, len(heights[r])-1):
            v = heights[r][c]
            if v < heights[r-1][c] and v < heights[r+1][c] and v < heights[r][c-1] and v < heights[r][c+1]:
                coord_list.append((r,c))
    return coord_list

def goto_deepest(heights, deepest, r, c):
    while (r, c) not in deepest:
        if heights[r-1][c] < heights[r][c]:
            r = r - 1
        elif heights[r+1][c] < heights[r][c]:
            r = r + 1
        elif heights[r][c-1] < heights[r][c]:
            c = c - 1
        elif heights[r][c+1] < heights[r][c]:
            c = c + 1
        else:
            print(f"error: no deeper point detected on {r}, {c}")
    return r, c

def solve_1(data):
    heights = parse_data(data)
    lowest = all_deepest(heights)
    risk_sum = 0
    for r,c in lowest:
        risk_sum += heights[r][c] + 1
    return risk_sum

def solve_2(data):
    heights = parse_data(data)
    deepest = all_deepest(heights)
    basins = {d: 0 for d in deepest}
    for r in range(1, len(heights)-1):
        for c in range(1, len(heights[r])-1):
            if heights[r][c] != 9:
                dr, dc = goto_deepest(heights, deepest, r, c)
                basins[(dr, dc)] += 1
    sizes = sorted(basins.values(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
