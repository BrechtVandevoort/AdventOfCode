import itertools

def get_different(box_id1, box_id2):
    num_different = 0
    same = ""
    for a,b in zip(box_id1, box_id2):
        if a != b:
            num_different += 1
        else:
            same += a
    return num_different, same


with open("input.txt") as puzzle_input:
    box_ids = [line.strip() for line in puzzle_input]

for box_id1, box_id2 in itertools.combinations(box_ids, 2):
    num_different, same = get_different(box_id1, box_id2)
    if num_different == 1:
        print("The box ids are {} and {}. The answer is {}.".format(box_id1, box_id2, same))
        break
