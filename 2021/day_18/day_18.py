from copy import deepcopy

def parse_data(data):
    return list(map(eval, data))

def is_regular(n):
    return type(n) == int

def add_left(n, pos, value):
    pos = pos[:]
    while len(pos) > 0 and pos[-1] == 0:
        pos = pos[:-1]
    if len(pos) == 0:
        return
    pos[-1] = 0
    nested_n = n
    for i in pos[:-1]:
        nested_n = nested_n[i]
    if is_regular(nested_n[0]):
        nested_n[0] += value
    else:
        nested_n = nested_n[0]
        while not is_regular(nested_n[1]):
            nested_n = nested_n[1]
        nested_n[1] += value

def add_right(n, pos, value):
    pos = pos[:]
    while len(pos) > 0 and pos[-1] == 1:
        pos = pos[:-1]
    if len(pos) == 0:
        return
    pos[-1] = 1
    nested_n = n
    for i in pos[:-1]:
        nested_n = nested_n[i]
    if is_regular(nested_n[1]):
        nested_n[1] += value
    else:
        nested_n = nested_n[1]
        while not is_regular(nested_n[0]):
            nested_n = nested_n[0]
        nested_n[0] += value

def explode(n, pos, nested_n):
    left, right = nested_n
    add_left(n, pos, left)
    add_right(n, pos, right)
    nested = n
    for i in pos[:-1]:
        nested = nested[i]
    nested[pos[-1]] = 0

def try_explode(n, pos, nested_n):
    nesting = len(pos)
    if nesting == 4:
        explode(n, pos, nested_n)
        return True
    if not is_regular(nested_n[0]) and try_explode(n, pos + [0], nested_n[0]):
        return True
    if not is_regular(nested_n[1]) and try_explode(n, pos + [1], nested_n[1]):
        return True
    return False

def create_pair(reg_num):
    left = reg_num // 2
    right = left + reg_num % 2
    return [left, right]

def try_split(nested_n):
    if is_regular(nested_n[0]):
        if nested_n[0] >= 10:
            nested_n[0] = create_pair(nested_n[0])
            return True
    else:
        if try_split(nested_n[0]):
            return True
    if is_regular(nested_n[1]):
        if nested_n[1] >= 10:
            nested_n[1] = create_pair(nested_n[1])
            return True
    else:
        if try_split(nested_n[1]):
            return True
    return False

def reduce_number(n):
    while True:
        success = try_explode(n, [], n)
        if not success:
            success = try_split(n)
            if not success:
                break

def add_numbers(n1, n2):
    n = [n1, n2]
    reduce_number(n)
    return n

def magnitude(n):
    if is_regular(n):
        return n
    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])

def solve_1(data):
    numbers = parse_data(data)
    total = numbers[0]
    for n in numbers[1:]:
        total = add_numbers(total, n)
    return magnitude(total)
    
def solve_2(data):
    numbers = parse_data(data)
    max_mag = 0
    for i, n in enumerate(numbers):
        for j, m in enumerate(numbers):
            if i != j:
                n_copy = deepcopy(n)
                m_copy = deepcopy(m)
                max_mag = max(max_mag, magnitude(add_numbers(n_copy, m_copy)))
    return max_mag

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
