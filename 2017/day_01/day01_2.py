captcha = open('input.txt').read().strip()

l = len(captcha)
s = 0
for i,x in enumerate(captcha):
	if x == captcha[(i + l/2) % l]:
		s += int(x)

print('solution: %d' % (s,))
