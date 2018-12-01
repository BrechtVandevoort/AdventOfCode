freq_changes = []
with open("input.txt") as puzzle_input:
    for freq_change in puzzle_input:
        freq_changes.append(int(freq_change))

visited_freq = set()
current_freq = 0
freq_change_index = 0
while current_freq not in visited_freq:
    visited_freq.add(current_freq)
    current_freq += freq_changes[freq_change_index]
    freq_change_index = (freq_change_index + 1) % len(freq_changes)

print("The resulting value is {}".format(current_freq))
