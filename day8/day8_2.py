count = 0
for x in open('input.txt'):
    i = 0
    count += 4
    while i < len(x):
        if x[i] == '\\':
            i += 1
            count += 1 if x[i] == 'x' else 2
        i += 1
print count
