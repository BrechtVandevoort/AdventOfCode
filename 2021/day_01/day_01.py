
def solve_1(data):
    depths = list(map(int, data))
    count = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            count += 1
    return count

def solve_2(data):
    depths = list(map(int, data))
    windows = []
    for i in range(1, len(depths)-1):
        windows.append(sum(depths[i-1:i+2]))
    return solve_1(windows)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
