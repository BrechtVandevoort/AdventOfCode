from typing import DefaultDict


def parse_data(data):
    rules = {}
    for line in data[2:]:
        left, right = line.split(" -> ")
        rules[left] = right
    polymer = data[0]
    pairs = {}
    for pair in rules:
        pairs[pair] = polymer.count(pair)
    return polymer, rules, pairs

# def apply_step(polymer, rules):
#     result = polymer[0]
#     for c in polymer[1:]:
#         pair = result[-1] + c
#         result += rules[pair] + c
#     return result

def apply_step(pairs, rules):
    new_pairs = {pair: 0 for pair in rules}
    for pair in pairs:
        mid = rules[pair]
        left = pair[0] + mid
        right = mid + pair[1]
        new_pairs[left] += pairs[pair]
        new_pairs[right] += pairs[pair]
    return new_pairs

def occurrences(pairs, polymer):
    counts = DefaultDict(int)
    for pair, count in pairs.items():
        counts[pair[0]] += count
        counts[pair[1]] += count
    counts[polymer[0]] += 1
    counts[polymer[-1]] += 1
    for c in counts:
        counts[c] //= 2
    return counts

def solve_1(data):
    polymer, rules, pairs = parse_data(data)
    for _ in range(10):
        pairs = apply_step(pairs, rules)
    occs = occurrences(pairs, polymer)
    return max(occs.values()) - min(occs.values())

def solve_2(data):
    polymer, rules, pairs = parse_data(data)
    for _ in range(40):
        pairs = apply_step(pairs, rules)
    occs = occurrences(pairs, polymer)
    return max(occs.values()) - min(occs.values())

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
