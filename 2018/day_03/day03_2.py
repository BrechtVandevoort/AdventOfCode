import re

def is_1D_overlap(x1, dx1, x2, dx2):
    return x1 + dx1 - 1 >= x2 and x2 + dx2 - 1 >= x1


claims = []
with open("input.txt") as puzzle_input:
    for line in puzzle_input:
        parts = re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line).groups()
        parts = tuple(map(int, parts))
        claims.append(parts)

for claim_id1, x1, y1, dx1, dy1 in claims:
    overlapping = False
    for claim_id2, x2, y2, dx2, dy2 in claims:
        if claim_id1 == claim_id2:
            continue
        if is_1D_overlap(x1, dx1, x2, dx2) and is_1D_overlap(y1, dy1, y2, dy2):
            overlapping = True
            break
    if not overlapping:
        print("Claim {} doesn't overlap with other claims.".format(claim_id1))
