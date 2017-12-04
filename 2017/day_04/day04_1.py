passphrases = [x.strip() for x in open('input.txt')]
correct = 0

for passphrase in passphrases:
	seen = set()
	invalid = False
	for word in passphrase.split():
		if word in seen:
			invalid = True
		seen.add(word)
	if not invalid:
		correct += 1

print correct
