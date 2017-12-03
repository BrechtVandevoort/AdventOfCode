triangles = map(lambda x: sorted(map(int, x.split())), open('input.txt').readlines())
print sum(1 for triangle in triangles if sum(triangle[:2]) > triangle[2])
