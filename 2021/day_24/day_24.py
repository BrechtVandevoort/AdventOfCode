from dataclasses import dataclass
from typing import List

@dataclass
class FragmentParam:
    z_div: int
    x_add: int
    y_add: int

def parse_data(data) -> List[FragmentParam]:
    fragment_params = []
    for _ in range(14):
        z_div = int(data[4].split()[2])
        x_add = int(data[5].split()[2])
        y_add = int(data[15].split()[2])
        data = data[18:]
        fragment_params.append(FragmentParam(z_div, x_add, y_add))
    assert(len(data) == 0)
    return fragment_params


# def exec_fragment(w, z, z_div, x_add, y_add) -> int:
#     x = z % 26 + x_add
#     z //= z_div
#     if x != w:
#         z *= 26
#         z += w + y_add
#     return z

# def exec_fragment_v2(w, z_stack, z_div, x_add, y_add):
#     if z_stack:
#         x = z_stack[-1] + x_add
#     else:
#         x = x_add
#     if z_div == 26:
#         z_stack = z_stack[:-1]
#     if x != w:
#         z_stack = z_stack + [w + y_add]
#     return z_stack[:]

def check_append_conditions(fragment_params: List[FragmentParam]):
    for fp in fragment_params:
        print(f"{repr(fp):<45s} does not append if prev z between {1-fp.x_add:<3} and {9 - fp.x_add:<3}. Otherwise appends between {1+fp.y_add:<3} and {9+fp.y_add:<3}")

def solve_1(data):
    fragment_params = parse_data(data)

    #check_append_conditions(fragment_params)

    answer = [0] * 14
    for i, fp in enumerate(fragment_params):
        if fp.z_div == 1:
            nesting = 0
            for j, fp2 in enumerate(fragment_params[i+1:]):
                if fp2.z_div == 1:
                    nesting += 1
                elif fp2.z_div == 26 and nesting > 0:
                    nesting -= 1
                else:
                    for c in range(9, 0, -1):
                        z = c + fp.y_add # fp appends this value
                        w2 = z + fp2.x_add # value needed to have fp2 not appending
                        if 1 <= w2 <= 9:
                            answer[i] = c
                            answer[i+1+j] = w2
                            break
                    break
    return "".join(map(str,answer))

def solve_2(data):
    fragment_params = parse_data(data)

    answer = [0] * 14
    for i, fp in enumerate(fragment_params):
        if fp.z_div == 1:
            nesting = 0
            for j, fp2 in enumerate(fragment_params[i+1:]):
                if fp2.z_div == 1:
                    nesting += 1
                elif fp2.z_div == 26 and nesting > 0:
                    nesting -= 1
                else:
                    for c in range(1, 10):
                        z = c + fp.y_add # fp appends this value
                        w2 = z + fp2.x_add # value needed to have fp2 not appending
                        if 1 <= w2 <= 9:
                            answer[i] = c
                            answer[i+1+j] = w2
                            break
                    break
    return "".join(map(str,answer))

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
