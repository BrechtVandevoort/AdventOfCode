import itertools

DISPLAY_VALUES = {
    frozenset("abcefg"): "0",
    frozenset("cf"): "1",
    frozenset("acdeg"): "2",
    frozenset("acdfg"): "3",
    frozenset("bcdf"): "4",
    frozenset("abdfg"): "5",
    frozenset("abdefg"): "6",
    frozenset("acf"): "7",
    frozenset("abcdefg"): "8",
    frozenset("abcdfg"): "9"
}

def parse_data(data):
    result = []
    for line in data:
        left, right = line.split("|")
        result.append((left.split(), right.split()))
    return result

def get_digit(values):
    if values in DISPLAY_VALUES:
        return DISPLAY_VALUES[values]
    return None

def rewire(display, mapping):
    new_display = ""
    letters = "abcdefg"
    for c in display:
        new_display += letters[mapping.index(c)]
    return get_digit(frozenset(new_display))

def untangle_entry(entry):
    patterns = entry[0] + entry[1]
    for mapping in itertools.permutations("abcdefg"):
        is_ok = True
        for display in patterns:
            if rewire(display, mapping) is None:
                is_ok = False
        if is_ok:
            output = ""
            for display in entry[1]:
                output += rewire(display, mapping)
            return int(output)

def solve_1(data):
    patterns = parse_data(data)
    count = 0
    for _, output in patterns:
        for symb in output:
            if len(symb) in (2,3,4,7):
                count += 1
    return count

def solve_2(data):
    patterns = parse_data(data)
    return sum(untangle_entry(p) for p in patterns)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
