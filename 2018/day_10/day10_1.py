import re

def read_input():
    points = []
    with open("input.txt") as puzzle_input:
        for line in puzzle_input:
            values = re.findall("-?\d+", line)
            values = list(map(int, values))
            points.append([(values[0], values[1]), (values[2], values[3])])
    return points


def update_points(points):
    updated = []
    for point in points:
        new_pos = (point[0][0] + point[1][0], point[0][1] + point[1][1])
        updated.append([new_pos, point[1]])
    return updated


def visualize_points(points):
    min_x = min(p[0][0] for p in points)
    max_x = max(p[0][0] for p in points)
    min_y = min(p[0][1] for p in points)
    max_y = max(p[0][1] for p in points)
    
    #only visualize if reasonable dimensions:
    if max_x - min_x > 100 or max_y - min_y > 20:
        return False
    
    positions = set(p[0] for p in points)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in positions:
                print('#', end="")
            else:
                print(' ', end="")
        print()
    return True

points = read_input()

#Keep iterating until manually ended
while True:
    while not visualize_points(points):
        points = update_points(points)
    input()
    points = update_points(points)
