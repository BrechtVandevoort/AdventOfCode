def parse_data(data):
    pattern = re.compile("(\d+)-(\d+) (\w): (\w+)")
    result = [re.match(pattern, s).groups() for s in data]
    return result

def solve_1(puzzle_input):
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1
    while len(recipes) < int(puzzle_input) + 10:
        r1 = recipes[elf1]
        r2 = recipes[elf2]
        new_recipes = r1 + r2
        for c in str(new_recipes):
            recipes.append(int(c))
        elf1 = (elf1 + r1 + 1) % len(recipes)
        elf2 = (elf2 + r2 + 1) % len(recipes)
    return "".join(map(str, recipes[int(puzzle_input):int(puzzle_input)+10]))

def solve_2(puzzle_input):
    recipes = [3, 7]
    elf1 = 0
    elf2 = 1
    while puzzle_input not in "".join(map(str, recipes[-10:])):
        r1 = recipes[elf1]
        r2 = recipes[elf2]
        new_recipes = r1 + r2
        for c in str(new_recipes):
            recipes.append(int(c))
        elf1 = (elf1 + r1 + 1) % len(recipes)
        elf2 = (elf2 + r2 + 1) % len(recipes)
    recipes_str = "".join(map(str, recipes))
    return recipes_str.find(puzzle_input)

def main():
    puzzle_input = "084601"
    print(f"Solution part 1: {solve_1(puzzle_input)}")
    print(f"Solution part 2: {solve_2(puzzle_input)}")

if __name__ == '__main__':
    main()
