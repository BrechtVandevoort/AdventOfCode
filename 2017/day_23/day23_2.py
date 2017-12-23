b = 67 * 100 + 100000
c = b + 17000
h = 0

def not_prime(b):
	for d in xrange(2, b):
		if b % d == 0:
			return True
	return False

for x in xrange(b, c + 17, 17):
	if not_prime(x):
		h += 1

print h