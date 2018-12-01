result = 0
with open("input.txt") as puzzle_input:
    for freq_change in puzzle_input:
        result += int(freq_change)
print("The resulting value is {}".format(result))
