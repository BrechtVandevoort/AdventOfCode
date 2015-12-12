e = lambda x: sum(map(e,x.values())) if isinstance(x,dict) and not 'red' in x.values() else sum(map(e,x)) if isinstance(x,list) else x if isinstance(x,int) else 0
print e(eval(''.join(open('input.txt'))))
