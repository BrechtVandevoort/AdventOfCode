gen_a, gen_b = 634, 301
matches = 0

for _ in xrange(5000000):
	gen_a = gen_a * 16807 % 2147483647
	while gen_a % 4 != 0:
		gen_a = gen_a * 16807 % 2147483647
	gen_b = gen_b * 48271 % 2147483647
	while gen_b % 8 != 0:
		gen_b = gen_b * 48271 % 2147483647
	if gen_a & 0xffff == gen_b & 0xffff:
		matches += 1

print matches