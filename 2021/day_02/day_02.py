
def solve_1(data):
    instructions = list(map(lambda x: x.split(), data))
    pos = 0
    depth = 0
    for instr, val in instructions:
        val = int(val)
        if instr == "forward":
            pos += val
        elif instr == "down":
            depth += val
        else:
            depth -= val
    return pos * depth

def solve_2(data):
    instructions = list(map(lambda x: x.split(), data))
    pos = 0
    depth = 0
    aim = 0
    for instr, val in instructions:
        val = int(val)
        if instr == "forward":
            pos += val
            depth += aim * val
        elif instr == "down":
            aim += val
        else:
            aim -= val
    return pos * depth

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
