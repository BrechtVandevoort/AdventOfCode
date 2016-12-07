import re

def split_parts(address):
	parts = re.split('\[|\]', address)
	if address[0] == '[':
		return parts[1::2], parts[::2]
	else:
		return parts[::2], parts[1::2]

def get_ABA(s):
	parts = set()
	for i in range(len(s) - 2):
		if s[i] == s[i+2] and s[i] != s[i+1]:
			parts.add(s[i:i+3])
	return parts

def convert_BAB(aba):
	return map(lambda s: s[1] + s[0]  + s[1], aba)

addresses = [line.strip() for line in open('input.txt').readlines()]
count = 0
for address in addresses:
	supernet, hypernet = split_parts(address)
	supernet_ABA = reduce(lambda s, part: s | get_ABA(part), supernet, set())
	hypernet_ABA = reduce(lambda s, part: s | get_ABA(part), hypernet, set())
	if not supernet_ABA.isdisjoint(convert_BAB(hypernet_ABA)):
		count += 1
print count
