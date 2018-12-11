#import sys
#sys.setrecursionlimit(10000)

def construct_tree(numbers):
    num_children = numbers[0]
    num_meta = numbers[1]
    numbers = numbers[2:]
    children = []
    for _ in range(num_children):
        child, numbers = construct_tree(numbers)
        children.append(child)
    meta = numbers[:num_meta]
    numbers = numbers[num_meta:]
    return (children, meta), numbers


def read_input():
    with open("input.txt") as puzzle_input:
        numbers = list(map(int, puzzle_input.read().split()))
    return numbers


def sum_meta(tree):
    children, meta = tree
    s = sum(meta)
    for child in children:
        s += sum_meta(child)
    return s


numbers = read_input()
tree, _ = construct_tree(numbers)
meta_sum = sum_meta(tree)
print("The sum is {}.".format(meta_sum))
