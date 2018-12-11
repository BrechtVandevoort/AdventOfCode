num_players = 478
max_marble = 71240

circle = [0, 1]
active_index = 1
player = 0
scores = [0 for _ in range(num_players)]

for marble in range(2, max_marble + 1):
    player = (player + 1) % num_players
    if marble % 23 != 0:
        active_index = (active_index + 2) % len(circle)
        circle.insert(active_index, marble)
    else:
        active_index = (active_index - 7) % len(circle)
        removed_marble = circle.pop(active_index)
        scores[player] += marble + removed_marble

print(max(scores))