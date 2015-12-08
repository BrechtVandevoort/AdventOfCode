count = 0
for x in open('input.txt'):
    i = 0
    count += 2
    while i < len(x):
        if x[i] == '\\':
            i += 1
            count += 3 if x[i] == 'x' else 1
        i += 1
print count
