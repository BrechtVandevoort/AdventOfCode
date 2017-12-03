captcha = open('input.txt').read().strip()

captcha += captcha[0]
s = 0
for i,x in enumerate(captcha[:-1]):
	if x == captcha[i+1]:
		s += int(x)

print('solution: %d' % (s,))
