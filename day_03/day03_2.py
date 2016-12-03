numbers = map(lambda x: map(int, x.split()), open('input.txt').readlines())
line_groups = zip(numbers[::3], numbers[1::3], numbers[2::3])
triangles = [sorted([group[0][i], group[1][i], group[2][i]]) for group in line_groups for i in range(3)]
print sum(1 for triangle in triangles if sum(triangle[:2]) > triangle[2])
