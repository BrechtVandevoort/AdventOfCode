def parse_data(data):
    i = 0
    while data[i] != "":
        i += 1
    dots = []
    for line in data[:i]:
        coords = line.split(",")
        coords = list(map(int, coords))
        dots.append(coords)
    folds = []
    for line in data[i+1:]:
        parts = line.split("=")
        fold = (parts[0][-1], int(parts[1]))
        folds.append(fold)
    return dots, folds

def apply_fold(dots, fold):
    pos = 0 if fold[0] == "x" else 1
    for dot in dots:
        diff = dot[pos] - fold[1]
        if diff > 0:
            dot[pos] = fold[1] - diff

def solve_1(data):
    dots, folds = parse_data(data)
    apply_fold(dots, folds[0])
    return len(set(map(tuple, dots)))

def solve_2(data):
    dots, folds = parse_data(data)
    for fold in folds:
        apply_fold(dots, fold)
    dot_set = set(map(tuple, dots))
    for row in range(max(d[1] for d in dot_set) + 1):
        for col in range(max(d[0] for d in dot_set) + 1):
            if (col, row) in dot_set:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
