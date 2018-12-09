def read_coords():
    coords = []
    with open("input.txt") as puzzle_input:
        for line in puzzle_input:
            coord = tuple(map(int, line.split(",")))
            coords.append(coord)
    return coords


def m_dist(coord1, coord2):
    return abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])


def get_closest_coords(point, coords):
    min_coords = []
    min_dist = None
    for coord in coords:
        dist = m_dist(coord, point)
        if min_dist is None or dist <= min_dist:
            if min_dist == dist:
                min_coords.append(coord)
            else:
                min_coords = [coord]
                min_dist = dist
    return min_coords


coords = read_coords()
coords_counter = {c: 0 for c in coords}

# All coordinates are strictly between 0 and 1000
for x in range(0,1001):
    for y in range(0,1001):
        min_coords = get_closest_coords((x,y), coords)
        if len(min_coords) == 1:
            coords_counter[min_coords[0]] += 1
            # Edge coordinates indicate infinite fields
            if x == 0 or x == 1000 or y == 0 or y == 1000:
                coords_counter[min_coords[0]] -= 1000000

print(max(coords_counter.values()))