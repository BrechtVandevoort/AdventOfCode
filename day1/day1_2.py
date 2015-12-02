l = raw_input()
print min([x for x,y in [(x,l[:x]) for x in [x+1 for x,y in enumerate(l)]] if sum([1 if z =='(' else -1 for z in y]) == -1])
