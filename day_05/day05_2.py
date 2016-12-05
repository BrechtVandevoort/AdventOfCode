import md5, random, string

def print_password(password):
	print '\r', ''.join(c if c != '*' else random.choice(string.letters) for c in password),

door_id = 'ffykfhsq'
password = ['*'] * 8
i = 0
print ''.join(password),
while '*' in password:
	h = md5.new(door_id + str(i)).hexdigest()
	if i % 1000 == 0:
		print_password(password)
	if h[:5] == '00000' and '0' <= h[5] < '8':
		pos = int(h[5])
		if password[pos] == '*':
			password[pos] = h[6]
			print_password(password)
	i += 1
print ''
