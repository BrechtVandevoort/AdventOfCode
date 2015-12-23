import re
d={'inc':'%(x)s+=1','hlf':'%(x)s/=2','tpl':'%(x)s*=3','jmp':'p+=%(x)s-1','jie':'p+=%(y)s-1 if %(x)s%%2==0 else 0','jio':'p+=%(y)s-1 if %(x)s==1 else 0'}
i=[re.match('(\w+) ([+-]?\w+),? ?(.*)',x).groups() for x in open('input.txt')]
a=1
b=0
p=0
while p>=0 and p<len(i):
    exec(d[i[p][0]]%{'x':i[p][1],'y':i[p][2]})
    p+=1
print b