

# Use 3 values to express rotations
# Negative values should be interpreted as negated value of the axis
X, Y, Z = 1, 2, 3

def rotx(v):
    a, b, c = v
    return (a, -c, b)

def roty(v):
    a, b, c = v
    return (c, b, -a)

def generate_rotations():
    v = (X, Y, Z)
    rotations = set()
    rotations.add(v)
    for _ in range(4):
        for _ in range(4):
            v = roty(v)
            rotations.add(v)
        v = rotx(v)
    
    v = roty(rotx(v))

    for _ in range(4):
        for _ in range(4):
            v = roty(v)
            rotations.add(v)
        v = rotx(v)
    
    return rotations

def apply_rotation(v, rot):
    w = ()
    for r in rot:
        axis = abs(r)
        sign = r // axis
        w += (sign * v[axis-1],)
    return w

def parse_data(data):
    scanners = []
    scanner = []
    for line in data:
        if len(line) == 0:
            continue
        if line[0:3] == "---":
            if len(scanner) > 0:
                scanners.append(scanner)
                scanner = []
        else:
            scanner.append(eval(line))
    scanners.append(scanner)
    return scanners

def translate(v, t):
    a1, b1, c1 = v
    a2, b2, c2 = t
    return (a1+a2, b1+b2, c1+c2)

def translation_vector(v1, v2):
    # translation vector from v1 towards v2
    return (v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2])

def try_beacon(beacons, rotated, beacon):
    for b in beacons:
        trans = translation_vector(beacon, b)
        #print(trans)
        translated = set(map(lambda x: translate(x, trans), rotated))
        known = beacons & translated
        #print(len(known))
        if len(known) >= 12:
            beacons |= translated
            return trans
    return None

def try_rotation(beacons, scanner, rot):
    rotated = list(map(lambda x: apply_rotation(x, rot), scanner))
    for b in rotated:
        result = try_beacon(beacons, rotated, b)
        if result is not None:
            return result
    return None

def try_append(beacons, scanner):
    possible_rotations = generate_rotations()
    for rot in possible_rotations:
        result = try_rotation(beacons, scanner, rot)
        if result is not None:
            return result
    return None

def get_beacons(scanners):
    beacons = set(scanners[0])
    scanner_positions = [(0, 0, 0)]
    remaining = scanners[1:]
    while remaining:
        for i, sc in enumerate(remaining):
            print(f"{len(remaining)} remaning: trying to append {i}")
            result = try_append(beacons, sc)
            if result is not None:
                remaining.pop(i)
                scanner_positions.append(result)
                break
        else:
            print("something wrong: unable to find next suitable scanner")
            break
    return beacons, scanner_positions

def solve_1(data):
    scanners = parse_data(data)
    return len(get_beacons(scanners)[0])

def solve_2(data):
    scanners = parse_data(data)
    scanner_positions = get_beacons(scanners)[1]
    print(scanner_positions)
    max_dist = 0
    for b1 in scanner_positions:
        for b2 in scanner_positions:
            dist = abs(b1[0]-b2[0]) + abs(b1[1]-b2[1]) + abs(b1[2]-b2[2])
            if dist > max_dist:
                print(b1, b2)
            max_dist = max(dist, max_dist)
    return max_dist

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    #print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
