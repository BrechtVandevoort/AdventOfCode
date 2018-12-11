grid_serial_number = 5791

def compute_power_level(x, y, grid_serial_number):
    # Convert to 1 indexed values
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level //= 100
    power_level %= 10
    power_level -= 5
    return power_level


def get_square_power(power_levels, x, y):
    power_level = 0
    for i in range(3):
        for j in range(3):
            power_level += power_levels[y + i][x + j]
    return power_level


power_levels = [[compute_power_level(x + 1, y + 1, grid_serial_number) for x in range(300)] for y in range(300)]

best_square = None
best_power_level = -999
for y in range(300-3):
    for x in range(300-3):
        power_level = get_square_power(power_levels, x, y)
        if power_level > best_power_level:
            best_square = (x + 1, y + 1)
            best_power_level = power_level

print("The answer is {},{}".format(best_square[0], best_square[1]))
