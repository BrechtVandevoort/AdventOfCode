def count_letters(box_id):
    counts = [0 for _ in range(26)]
    for c in box_id:
        counts[ord(c) - ord("a")] += 1
    return counts


with open("input.txt") as puzzle_input:
    box_ids = [line.strip() for line in puzzle_input]

count_2 = 0
count_3 = 0
for box_id in box_ids:
    counts = count_letters(box_id)
    if 2 in counts:
        count_2 += 1
    if 3 in counts:
        count_3 += 1
        
checksum = count_2 * count_3
print("The checksum is {}.".format(checksum))