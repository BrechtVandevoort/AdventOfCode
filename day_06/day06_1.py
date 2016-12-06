from collections import Counter

messages = [line.strip() for line in open('input.txt').readlines()]
counters = map(lambda pos: Counter(pos), zip(*messages))
print ''.join(c.most_common(1)[0][0] for c in counters)
