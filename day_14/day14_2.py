from hashlib import md5
from itertools import groupby
import re

puzzle_input = 'ihaygndm'
hash_dictionary = {}

def calc_hash(index):
	global hash_dictionary
	if index in hash_dictionary:
		return hash_dictionary[index]
	h = puzzle_input + str(index)
	for _ in xrange(2017):
		h = md5(h).hexdigest()
	hash_dictionary[index] = h
	return h

def get_same_3(s):
	for i in xrange(len(s) - 2):
			if s[i] == s[i+1] == s[i+2]:
				return s[i]
	return None

def has_same_5(s, target):
	for i in xrange(len(s) - 4):
			if target == s[i] == s[i+1] == s[i+2] == s[i+3] == s[i+4]:
				return True
	return False


keys = []
index = 0
while len(keys) < 64:
	h = calc_hash(index)
	target = get_same_3(h)
	if target:
		for i in xrange(1, 1001):
			m = calc_hash(index + i)
			if has_same_5(m, target):
				print len(keys), 'found'
				keys.append(index)
				break
	index += 1

print 'result:', keys[-1]
