import re

def remove_collisions(particles):
	removed = set()
	particles = map(tuple, particles)
	
	for i, p1 in enumerate(particles):
		for j, p2 in enumerate(particles):
			if i != j and p1[:3] == p2[:3]:
				removed.add(p1)
				removed.add(p2)
	
	return map(list, set(particles) - removed)

def update_particles(particles):
	for p in particles:
		p[3:6] = [v + a for v,a in zip(p[3:6], p[6:9])]
		p[:3] = [x + v for x,v in zip(p[:3], p[3:6])]

lines = open('input.txt').readlines()
particles = [map(int, re.findall('-?\d+', l)) for l in lines]

while True:
	print len(particles)
	particles = remove_collisions(particles)
	update_particles(particles)