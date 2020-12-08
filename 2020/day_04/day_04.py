import re

type_checks = {
    "byr": lambda v: 1920 <= int(v) <= 2002,
    "iyr": lambda v: 2010 <= int(v) <= 2020,
    "eyr": lambda v: 2020 <= int(v) <= 2030,
    "hgt": lambda v: v[-2:] == "cm" and 150 <= int(v[:-2]) <= 193 or v[-2:] == "in" and 59 <= int(v[:-2]) <= 76,
    "hcl": lambda v: re.fullmatch("#[0-9a-f]{6}", v) is not None,
    "ecl": lambda v: v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda v: re.fullmatch(r"\d{9}", v) is not None,
    "cid": lambda v: True
}

def valid_types(fields):
    for field in fields:
        f_type, value = field.split(":", 1)
        try:
            if not type_checks[f_type](value):
                return False
        except:
            return False
    return True

def is_valid(passport, value_check=False):
    required_types = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    fields = passport.split()
    types = set(f[:3] for f in fields)
    if required_types.issubset(types):
        return not value_check or valid_types(fields)

def solve(data, value_check=False):
    passports = data.replace(" ", "\n").strip().split("\n\n")
    num_valid = 0
    for pp in passports:
        if is_valid(pp, value_check):
            num_valid += 1
    return num_valid

def solve_1(data):
    return solve(data)

def solve_2(data):
    return solve(data, True)

def main():
    with open("input.txt") as fp:
        data = fp.read()
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
