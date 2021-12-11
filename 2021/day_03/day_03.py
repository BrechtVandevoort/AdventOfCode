def count_values(numbers, pos):
    num_ones = sum(map(int, [n[pos] for n in numbers]))
    num_zeros = len(numbers) - num_ones
    return num_zeros, num_ones

def apply_bit_criteria(numbers, criteria):
    pos = 0
    while len(numbers) > 1:
        nz, no = count_values(numbers, pos)
        numbers = [n for n in numbers if criteria(n[pos], nz, no)]
        pos += 1
    return numbers[0]

def ox_criteria(digit, num_zeros, num_ones):
    if num_ones >= num_zeros:
        return digit == "1"
    else:
        return digit == "0"

def co2_criteria(digit, num_zeros, num_ones):
    if num_ones >= num_zeros:
        return digit == "0"
    else:
        return digit == "1"

def solve_1(data):
    num_bits = len(data[0])
    gamma = ""
    epsilon = ""
    for i in range(num_bits):
        nz, no = count_values(data, i)
        if no > nz:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)

def solve_2(data):
    ox_val = apply_bit_criteria(data, ox_criteria)
    co2_val = apply_bit_criteria(data, co2_criteria)
    return int(ox_val, 2) * int(co2_val, 2)


def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
