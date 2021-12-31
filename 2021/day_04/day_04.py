def parse_data(data):
    numbers = data[0].split(",")
    data = data[1:]
    num_boards = len(data) // 6
    boards = []
    for i in range(num_boards):
        board_data = data[i*6+1:(i+1)*6]
        board = [s.split() for s in board_data]
        boards.append(board)
    return numbers, boards

def update_board(board, number):
    for row in board:
        for i, v in enumerate(row):
            if v == number:
                row[i] = "*"

def check_board(board):
    for row in board:
        if all(v == "*" for v in row):
            return True
    for c in range(len(board[0])):
        if all(row[c] == "*" for row in board):
            return True
    return False

def board_sum(board):
    s = 0
    for row in board:
        s += sum(int(v) for v in row if v != "*")
    return s

def solve_1(data):
    numbers, boards = parse_data(data)
    for n in numbers:
        for b in boards:
            update_board(b, n)
            if check_board(b):
                score = board_sum(b)
                return score * int(n)

def solve_2(data):
    numbers, boards = parse_data(data)
    for n in numbers:
        for b in boards:
            update_board(b, n)
            if all(check_board(b2) for b2 in boards):
                score = board_sum(b)
                return score * int(n)

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
