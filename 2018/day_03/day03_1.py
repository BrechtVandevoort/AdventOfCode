import re

claims = []
with open("input.txt") as puzzle_input:
    for line in puzzle_input:
        parts = re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line).groups()
        parts = tuple(map(int, parts))
        claims.append(parts)

FABRIC_SIZE = 1000
fabric = [[0 for _ in range(FABRIC_SIZE)] for _ in range(FABRIC_SIZE)]

for claim_id, x, y, dx, dy in claims:
    for i in range(y, y + dy):
        for j in range(x, x + dx):
            fabric[i][j] += 1

result = sum(1 for row in fabric for cell in row if cell > 1)
print("The result is {}.".format(result))
