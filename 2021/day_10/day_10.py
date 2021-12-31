CORR_SCORE_LOOKUP = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

COMPL_SCORE_LOOKUP = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

CLOSING_LOOKUP = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

def corruptness_score(line):
    stack = []
    for c in line:
        if c in CLOSING_LOOKUP:
            stack.append(c)
        else:
            if c != CLOSING_LOOKUP[stack.pop()]:
                return CORR_SCORE_LOOKUP[c]
    return 0

def completion_score(line):
    stack = []
    for c in line:
        if c in CLOSING_LOOKUP:
            stack.append(c)
        else:
            if c != CLOSING_LOOKUP[stack.pop()]:
                return 0
    result = 0
    for c in reversed(stack):
        result *= 5
        result += COMPL_SCORE_LOOKUP[CLOSING_LOOKUP[c]]
    return result

def solve_1(data):
    return sum(corruptness_score(l) for l in data)     

def solve_2(data):
    scores = [completion_score(l) for l in data]
    scores = sorted(s for s in scores if s > 0)
    return scores[len(scores) // 2]

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
