def parse_data(data):
    nums = list(map(int, data[0].split(",")))
    fish = [sum(1 for n in nums if n == i) for i in range(9)]
    return fish

def simulate_day(fish):
    new_fish = fish[0]
    for i in range(len(fish)-1):
        fish[i] = fish[i+1]
    fish[6] += new_fish
    fish[8] = new_fish

def solve(data, num_days):
    fish = parse_data(data)
    for _ in range(num_days):
        simulate_day(fish)
    return sum(fish)

def solve_1(data):
    return solve(data, 80)

def solve_2(data):
    return solve(data, 256)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
