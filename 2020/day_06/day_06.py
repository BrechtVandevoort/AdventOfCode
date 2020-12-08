
def anyone_yes(group):
    num_yes = set()
    for line in group:
        for c in line:
            num_yes.add(c)
    return len(num_yes)

def all_yes(group):
    count = 0
    for c in group[0].strip():
        for line in group:
            if c not in line:
                break
        else:
            count += 1
    return count

def solve_1(data):
    groups = data.split("\n\n")
    return sum(anyone_yes(g.split()) for g in groups)

def solve_2(data):
    groups = data.split("\n\n")
    return sum(all_yes(g.split()) for g in groups)

def main():
    with open("input.txt") as fp:
        data = fp.read().strip()
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
