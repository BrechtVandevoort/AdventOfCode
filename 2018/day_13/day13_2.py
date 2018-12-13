forward_dict = {"^": (-1,0),"v": (1,0), "<": (0,-1), ">": (0,1)}
rotate_left_dict = {"^": "<", "<": "v", "v": ">", ">": "^"}
rotate_right_dict = {"^": ">", "<": "^", "v": "<", ">": "v"}

def read_input():
    tracks = []
    carts = []
    with open("input.txt") as puzzle_input:
        y = 0
        for line in puzzle_input:
            line = line.strip("\n")
            x = 0
            track = ""
            for c in line:
                if c == "v" or c == "^":
                    carts.append([y, x, c, 0])
                    c = "|"
                elif c == "<" or c == ">":
                    carts.append([y, x, c, 0])
                    c = "-"
                track += c
                x += 1
            tracks.append(track)
            y += 1
    return tracks, carts


def move_forward(cart):
    delta = forward_dict[cart[2]]
    cart[0] += delta[0]
    cart[1] += delta[1]


def rotate_cart(cart):
    if cart[3] == 0:
        cart[2] = rotate_left_dict[cart[2]]
    elif cart[3] == 2:
        cart[2] = rotate_right_dict[cart[2]]
    cart[3] = (cart[3] + 1) % 3


def tick(tracks, carts):
    # Assume carts are in correct order for processing
    removed_indices = set()
    for i, cart in enumerate(carts):
        track = tracks[cart[0]][cart[1]]
        if track == "|" or track == "-":
            move_forward(cart)
        elif track == "/":
            if cart[2] == "^":
                cart[2] = ">"
            elif cart[2] == "v":
                cart[2] = "<"
            elif cart[2] == "<":
                cart[2] = "v"
            elif cart[2] == ">":
                cart[2] = "^"
            move_forward(cart)
        elif track == "\\":
            if cart[2] == "^":
                cart[2] = "<"
            elif cart[2] == "v":
                cart[2] = ">"
            elif cart[2] == "<":
                cart[2] = "^"
            elif cart[2] == ">":
                cart[2] = "v"
            move_forward(cart)
        elif track == "+":
            rotate_cart(cart)
            move_forward(cart)
        else:
            print("ERROR!")
        for j, c in enumerate(carts):
            if j != i and cart[0] == c[0] and cart[1] == c[1]:
                removed_indices.add(i)
                removed_indices.add(j)
    removed_indices = sorted(removed_indices, reverse=True)
    for r in removed_indices:
        carts.pop(r)


tracks, carts = read_input()
while len(carts) > 1:
    tick(tracks, carts)
    carts.sort()

print("Last cart at x: {}, y: {}.".format(carts[0][1], carts[0][0]))
