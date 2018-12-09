def read_coords():
    coords = []
    with open("input.txt") as puzzle_input:
        for line in puzzle_input:
            coord = tuple(map(int, line.split(",")))
            coords.append(coord)
    return coords


def m_dist(coord1, coord2):
    return abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])


coords = read_coords()
counter = 0

# All coordinates are strictly between 0 and 1000
for x in range(0,1001):
    for y in range(0,1001):
        total_dist = 0
        for coord in coords:
            total_dist += m_dist(coord, (x,y))
            if total_dist >= 10000:
                break
        if total_dist < 10000:
            counter += 1
            #Check if field is sufficiently large
            if x == 0 or x == 1000 or y == 0 or y == 1000:
                print("Error! Larger field needed.")

print(counter)