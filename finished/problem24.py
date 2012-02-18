# -*- coding:utf-8 -*-
# http://projecteuler.net/problem=24
# What is the millionth lexicographic permutation of the digits 
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Recursive function to generate the permutations.
# t is the current permutation on which we're working,
# set is the set of the numbers which can be added,
# generated is the big table containing all the permutations
def gen(t, set, generated):
	if len(set) == 0:
		generated.append(t)
	else:
		for n in set:
			copy_t = t[:] 	# copies t
			copy_s = set[:] # copies the set
			copy_s.remove(n)
			copy_t.append(n)
			gen(copy_t, copy_s, generated)
			
def generatePermutations(t):
	generated = []
	gen([], t, generated)
	return generated

permutations = generatePermutations([0,1,2,3,4,5,6,7,8,9])
# 1 000 000th is located at index 999 999
print "The solution is %s" % permutations[999999]
