
def sum_pair(values, value):
    for i, val1 in enumerate(values):
        for val2 in values[i+1:]:
            if val1 + val2 == value:
                return val1, val2
    return None

def solve_1(data):
    for i in range(25, len(data)):
        subset = data[i-25:i]
        value = data[i]
        if sum_pair(subset, value) is None:
            return value

def solve_2(data):
    answer_1 = solve_1(data)
    for i in range(len(data)):
        for j in range(i+2, len(data)):
            s = sum(data[i:j])
            if s == answer_1:
                return min(data[i:j]) + max(data[i:j])
            if s > answer_1:
                break

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: int(x.strip()), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
