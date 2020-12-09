
def simulate_code(instructions):
    acc = 0
    visited = []
    current_instr = 0
    while current_instr not in visited and 0 <= current_instr < len(instructions):
        visited.append(current_instr)
        instr, value = instructions[current_instr].split()
        value = int(value)
        if instr == "acc":
            acc += value
        elif instr == "jmp":
            current_instr += value - 1
        current_instr += 1
    return acc, current_instr == len(instructions)

def solve_1(data):
    return simulate_code(data)[0]

def solve_2(data):
    for i, line in enumerate(data):
        instr, value = line.split()
        if instr in ("jmp", "nop"):
            new_instr = "jmp" if instr == "nop" else "nop"
            new_instr += " " + value
            new_instructions = data[:i] + [new_instr] + data[i+1:]
            acc, success = simulate_code(new_instructions)
            if success:
                return acc

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
