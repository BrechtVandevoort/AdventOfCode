import md5
print (x for x in xrange(99999999) if md5.new('iwrupvqb'+str(x)).hexdigest()[:5]=='00000').next()
