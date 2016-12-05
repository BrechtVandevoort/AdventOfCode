import md5

door_id = 'ffykfhsq'
password = ''
i = 0
while len(password) < 8:
	h = md5.new(door_id + str(i)).hexdigest()
	if h[:5] == '00000':
		password += h[5]
	i += 1
print password
