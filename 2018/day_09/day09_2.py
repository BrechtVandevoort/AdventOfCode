from collections import deque

num_players = 478
max_marble = 71240 * 100

# Use deque for fast editing of list on both ends
# The active marble is always the first element
circle = deque([1, 0])
player = 0
scores = [0 for _ in range(num_players)]

for marble in range(2, max_marble + 1):
    player = (player + 1) % num_players
    if marble % 23 != 0:
        circle.rotate(-2)
        circle.appendleft(marble)
    else:
        circle.rotate(7)
        removed_marble = circle.popleft()
        scores[player] += marble + removed_marble

print(max(scores))