from collections import defaultdict
import itertools

def parse_data(data):
    player_1 = int(data[0][-2:])
    player_2 = int(data[1][-2:])
    return player_1, player_2

def create_dice():
    while True:
        for i in range(1, 101):
            yield i

def solve_1(data):
    p1, p2 = parse_data(data)
    s1, s2 = 0, 0
    die = create_dice()
    rolls = 0
    while True:
        throw = next(die) + next(die) + next(die)
        rolls += 3
        p1 = (p1 - 1 + throw) % 10 + 1
        s1 += p1
        if s1 >= 1000:
            break
        throw = next(die) + next(die) + next(die)
        rolls += 3
        p2 = (p2 - 1 + throw) % 10 + 1
        s2 += p2
        if s2 >= 1000:
            break
    return min(s1, s2) * rolls

def solve_2(data):
    # state: ((p1, p2), (s1, s2), turn, total_turns), where turn is either 0 (player 1) or 1 (player 2)
    start_p1, start_p2 = parse_data(data)
    states = defaultdict(int)
    states[((start_p1, start_p2), (0, 0), 0, 0)] = 1
    num_wins = [0, 0] #first elem is player 1, second is player 2
    # Iterate based on increasing score for player that needs to throw next (avoiding handling the same state multiple times)
    handled = set()
    for i in range(21):
        for positions, scores, t, total in states.copy():
            if total != i:
                continue
            assert((positions, scores, t, total) not in handled)
            handled.add((positions, scores, t, total))
            num_universes = states[(positions, scores, t, total)]
            for d in itertools.product((1,2,3), repeat=3):
                throw = sum(d)
                p = (positions[t] + throw - 1) % 10 + 1
                s = scores[t] + p
                if s >= 21:
                    num_wins[t] += num_universes
                else:
                    p1, p2 = positions
                    s1, s2 = scores
                    if t == 0:
                        states[((p, p2), (s, s2), 1, total+1)] += num_universes
                        assert(((p, p2), (s, s2), 1, total+1) not in handled)
                    else:
                        states[((p1, p), (s1, s), 0, total+1)] += num_universes
                        assert(((p1, p), (s1, s), 0, total+1) not in handled)
    return max(num_wins)
 
def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
