def parse_data(data):
    return list(map(int, data[0].split(",")))


def solve(data, dist_cost_f):
    positions = parse_data(data)
    best = None
    cost = None
    for i in range(min(positions), max(positions)+1):
        new_cost = sum(dist_cost_f(p, i) for p in positions)
        if cost is None or new_cost < cost:
            cost = new_cost
            best = i
    return cost

def solve_1(data):
    f = lambda x, y: abs(x - y)
    return solve(data, f)

def solve_2(data):
    f = lambda x, y: abs(x - y) * (abs(x - y) + 1) // 2
    return solve(data, f)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
