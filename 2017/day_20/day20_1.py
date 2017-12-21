import re
lines = open('input.txt').readlines()
particles = [map(int, re.findall('-?\d+', l)) for l in lines]

particle_acc = [sum(map(abs, p[6:9])) for p in particles]
min_acc = min(particle_acc)

print particle_acc.index(min_acc)