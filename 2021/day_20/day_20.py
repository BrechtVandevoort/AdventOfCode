

def create_enhancement(img_enh_algo):
    enhancement = {}
    for i, value in enumerate(img_enh_algo):
        # convert i to 9 digit binary representation
        i_binary = f"{i:0>9b}"
        value_binary = "0" if value == "." else "1"
        enhancement[i_binary] = value_binary
    return enhancement

def create_image(img_data):
    image = []
    for line in img_data:
        new_line = line.replace("#", "1").replace(".", "0")
        image.append(new_line)
    return image

def parse_data(data):
    enhancement = create_enhancement(data[0])
    image = create_image(data[2:])
    return enhancement, image

def enlarge_image(image, outside_fields):
    new_image = []
    row_length = len(image[0]) + 2
    new_image.append(outside_fields * row_length)
    for line in image:
        new_image.append(outside_fields + line + outside_fields)
    new_image.append(outside_fields * row_length)
    return new_image

def update_field(enhancement, image, outside_fields, row, col):
    lookup = ""
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if 0 <= r < len(image) and 0 <= c < len(image[r]):
                lookup += image[r][c]
            else:
                lookup += outside_fields
    return enhancement[lookup]

def one_pass(enhancement, image, outside_fields):
    new_image = []
    for r, line in enumerate(image):
        new_line = ""
        for c, value in enumerate(line):
            new_line += update_field(enhancement, image, outside_fields, r, c)
        new_image.append(new_line)
    new_outside_fields = enhancement[outside_fields * 9]
    return new_image, new_outside_fields

def solve_1(data):
    enhancement, image = parse_data(data)
    outside_fields = "0"
    for _ in range(2):
        image = enlarge_image(image, outside_fields)
        image, outside_fields = one_pass(enhancement, image, outside_fields)
    s = 0
    for line in image:
        for value in line:
            s += int(value)
    return s

def solve_2(data):
    enhancement, image = parse_data(data)
    outside_fields = "0"
    for _ in range(50):
        image = enlarge_image(image, outside_fields)
        image, outside_fields = one_pass(enhancement, image, outside_fields)
    s = 0
    for line in image:
        for value in line:
            s += int(value)
    return s

def main():
    with open("input.txt") as fp:
        data = list(map(lambda x: x.strip(), fp.readlines()))
    print(f"Solution part 1: {solve_1(data)}")
    print(f"Solution part 2: {solve_2(data)}")

if __name__ == '__main__':
    main()
