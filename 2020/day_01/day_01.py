import itertools
import math

def solve(data, num_reps):
    numbers = map(int, data)
    for n in itertools.combinations(numbers, num_reps):
        if sum(n) == 2020:
            return math.prod(n)

def solve_1(data):
    return solve(data, 2)

def solve_2(data):
    return solve(data, 3)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(solve_1(data))
    print(solve_2(data))

if __name__ == '__main__':
    main()
