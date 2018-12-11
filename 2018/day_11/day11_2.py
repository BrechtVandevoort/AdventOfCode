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


power_levels = [[compute_power_level(x + 1, y + 1, grid_serial_number) for x in range(300)] for y in range(300)]
square_power = {(x,y,1): power_levels[y][x] for y in range(300) for x in range(300)}

#Dynamic programming: power levels of larger squares are constructed from 4 smaller squares
for size in range(2, 301):
    for y in range(300 - size + 1):
        for x in range(300 - size + 1):
            if size % 2 == 0:
                # Split square in 4 equal squares
                power_level = square_power[(x, y, size//2)]
                power_level += square_power[(x, y + size//2, size//2)]
                power_level += square_power[(x + size//2, y, size//2)]
                power_level += square_power[(x + size//2, y + size//2, size//2)]
            else:
                # If size is odd, use 2 larger and two smaller squares,
                # so that only the middle value is covered by two squares instead of one
                power_level = square_power[(x, y, size//2 + 1)]
                power_level += square_power[(x + size//2, y + size//2, size//2+1)]
                power_level += square_power[(x, y + size//2 + 1, size//2)]
                power_level += square_power[(x + size//2 + 1, y, size//2)]
                # Compensate for value counted twice
                power_level -= square_power[(x + size//2, y + size//2, 1)]
            square_power[(x, y, size)] = power_level


best_square = None
best_value = -999
for key, value in square_power.items():
    if value > best_value:
        best_square = key
        best_value = value

print("The answer is {},{},{}".format(best_square[0] + 1, best_square[1] + 1, best_square[2]))
