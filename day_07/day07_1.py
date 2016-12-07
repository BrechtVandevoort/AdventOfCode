import re

def has_ABBA(s):
	for i in range(len(s) - 3):
		if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
			return True
	return False

addresses = [line.strip() for line in open('input.txt').readlines()]
count = 0
for address in addresses:
	found = False
	for part in re.split('\[|\]', address):
		if has_ABBA(part):
			found = True
	for part in re.findall('\[[a-z]*\]', address):
		if has_ABBA(part[1:-1]):
			found = False
	if found:
		count += 1
print count
