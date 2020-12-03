class Square:

    def __init__(self, value, elf_attack=3):
        self.value = value
        self.hitpoints = 0
        self.hp = 0
        if self.value == "E" or self.value == "G":
            self.hitpoints = 3
            self.hp = 200
        if self.value == "E":
            self.hitpoints = elf_attack

    def is_unit(self):
        return self.hp > 0

    def is_enemy(self, square):
        return self.is_unit() and square.is_unit() and self.value != square.value

    def attack(self, square):
        square.hp -= self.hitpoints
        if square.hp <= 0:
            square.value = "."
            square.hitpoints = 0
            square.hp = 0

    def is_empty(self):
        return self.value == "."

def neighbour_coords(field, coords):
    neighbours = []
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for r, c in directions:
        r += coords[0]
        c += coords[1]
        if 0 <= r < len(field) and 0 <= c < len(field[r]):
            neighbours.append((r, c))
    return neighbours


def neighbour_enemies(field, coords):
    square = field[coords[0]][coords[1]]
    neighbours = []
    for r, c in neighbour_coords(field, coords):
        if square.is_enemy(field[r][c]):
            neighbours.append(field[r][c])
    return neighbours

def play_order(field):
    coords = []
    for r, row in enumerate(field):
        for c, square in enumerate(row):
            if square.is_unit():
                coords.append((r, c))
    return coords

def check_enemies(field, square):
    for row in field:
        for sq in row:
            if square.is_enemy(sq):
                return True
    return False

def expand_dist_matrix(field, dist_matrix, coords):
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    visited = [coords]
    border = [coords]
    while len(border) > 0:
        b_r, b_c = border.pop(0)
        value = dist_matrix[b_r][b_c]
        for r, c in directions:
            r += b_r
            c += b_c
            if 0 <= r < len(dist_matrix) and 0 <= c < len(dist_matrix[r]):
                if field[r][c].is_empty() and (r, c) not in visited:
                    if dist_matrix[r][c] is None or dist_matrix[r][c] > value + 1:
                        dist_matrix[r][c] = value + 1
                        border.append((r,c))
                        visited.append((r,c))

def find_target(field, coords):
    square = field[coords[0]][coords[1]]
    dist_matrix = [[None for v in row] for row in field]
    dist_matrix[coords[0]][coords[1]] = 0
    expand_dist_matrix(field, dist_matrix, coords)
    closest_target = None
    closest_distance = None
    for r, row in enumerate(dist_matrix):
        for c, dist in enumerate(row):
            if dist is not None and (closest_distance is None or dist < closest_distance):
                has_neighbour = False
                for nb_r, nb_c in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    nb_r += r
                    nb_c += c
                    if square.is_enemy(field[nb_r][nb_c]):
                        has_neighbour = True
                if has_neighbour:
                    closest_distance = dist
                    closest_target = (r, c)
    return closest_target

def next_step(field, coords, target_coords):
    dist_matrix = [[None for v in row] for row in field]
    dist_matrix[target_coords[0]][target_coords[1]] = 0
    expand_dist_matrix(field, dist_matrix, target_coords)
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    new_coords = None
    new_dist = None
    for r, c in directions:
        r += coords[0]
        c += coords[1]
        if 0 <= r < len(dist_matrix) and 0 <= c < len(dist_matrix[r]):
            dist = dist_matrix[r][c]
            if dist is not None and (new_coords is None or new_dist > dist):
                new_coords = (r, c)
                new_dist = dist
    return new_coords

def move(field, coords):
    square = field[coords[0]][coords[1]]
    target_coords = find_target(field, coords)
    if target_coords is not None:
        move_to = next_step(field, coords, target_coords)
        field[move_to[0]][move_to[1]] = square
        field[coords[0]][coords[1]] = Square(".")
        coords = move_to
    return coords

def play(field, coords):
    square = field[coords[0]][coords[1]]
    if square.is_unit():
        if not check_enemies(field, square):
            return False
        if len(neighbour_enemies(field, coords)) == 0:
            coords = move(field, coords)
        weakest_nb = None
        for nb in neighbour_enemies(field, coords):
            if weakest_nb is None or weakest_nb.hp > nb.hp:
                weakest_nb = nb
        if weakest_nb is not None:
            square.attack(weakest_nb)
    return True

def print_field(field):
    for row in field:
        for sq in row:
            print(sq.value, end="")
        print()

def count_elves(field):
    return sum(1 for r in field for sq in r if sq.value == "E")

def simulate_battle(data, elf_attack=3, stop_if_elf_dies=False):
    field = [[Square(c, elf_attack) for c in row] for row in data]
    num_elves = count_elves(field)
    completed_rounds = 0
    while True:
        print(f"started round {completed_rounds + 1}")
        print_field(field)
        enemies_remaining = True
        for coords in play_order(field):
            if not play(field, coords):
                enemies_remaining = False
        if not enemies_remaining:
            break
        completed_rounds += 1
        if count_elves(field) < num_elves and stop_if_elf_dies:
            break
    print(f"{completed_rounds} completed_rounds rounds")
    remaining_hp = sum(sq.hp for row in field for sq in row if sq.is_unit())
    print(f"{remaining_hp} remaining hp")
    answer = completed_rounds * remaining_hp
    num_elves = 0
    for row in field:
        for sq in row:
            if sq.value == "E":
                num_elves += 1
    return answer, num_elves

def solve_1(data):
    return simulate_battle(data)[0]

def solve_2(data):
    num_elves = sum(1 for row in data for c in row if c == "E")
    remaining = 0
    elf_attack = 3
    while remaining < num_elves:
        elf_attack += 1
        score, remaining = simulate_battle(data, elf_attack=elf_attack, stop_if_elf_dies=True)
    return score

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
