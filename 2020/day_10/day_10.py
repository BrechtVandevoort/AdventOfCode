
def num_combinations(jolts, remaining, memoization):
    if (jolts, remaining) in memoization:
        return memoization[(jolts, remaining)]
    if len(remaining) <= 1:
        return len(remaining)
    # combinations with first adapter
    combis = num_combinations(remaining[0], remaining[1:], memoization)
    # combinations without first adapter only if we can skip it
    if jolts + 3 >= remaining[1]:
        combis += num_combinations(jolts, remaining[1:], memoization)
    memoization[(jolts, remaining)] = combis
    return combis

def solve_1(data):
    diffs = [j-i for i, j in zip([0] + data, data + [data[-1] + 3])]
    return diffs.count(1) * diffs.count(3)

def solve_2(data):
    memoization = {}
    return num_combinations(0, tuple(data), memoization)

def main():
    with open("input.txt") as fp:
        data = sorted(map(lambda x: int(x.strip()), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
