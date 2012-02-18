# -*- coding:utf-8 -*-
# http://projecteuler.net/problem=30
# Find the sum of all the numbers that can be written as the sum of 
# fifth powers of their digits.

# I've found two solutions. One is complicated to understand but is
# fast, the other one is naive (brute force) but fast enough for little
# values of power.
power = 5
	
# this recursive function generates the solutions.
# digitsNumber is the number of digits to generate (this parameter
# 	decreases as the recursive calls are made)
# t is the actual candidate number, as a table of digits
# digits is the set of the authorized digits to add at the end of the
# 	actual generated number.
# generated contains all the previous solutions.
def gen(digitsNumber, t, digits, generated):
	if digitsNumber == 0:
		# if there is no more digits to add, we have to test the number.
		# It has the form [a1, a2, a3, ...] where a1 <= a2 <= a3 etc...
		
		# computes the sum of fifth powers of digits
		n = reduce(lambda x,y:x+y, [c**power for c in t])
		# retrieves the digits of n and puts them in a table as chars.
		# for instance : if n == 12354, comp_t == [1, 2, 3, 5, 4]
		comp_t = [int(c) for c in str(n)]
		comp_t.sort()
		
		# if the digits of the computed table and the origin table are
		# the same, we've got a solution !
		if len(comp_t) == len(t) and comp_t == t:
			generated.append(n)
	else:
		# this part generates the [a1, a2, a3, a4, etc...] where a1,...
		# , a4, etc... are the digits, in lexicographic order.
		copy_digits = digits
		for d in digits:
			copy_t = t[:]
			copy_t.append(d)
			copy_digits = copy_digits[:]
			gen(digitsNumber - 1, copy_t, copy_digits, generated)
			copy_digits.remove(d)
			
# inits the recursive call and returns the generated solutions
def generate(size):
	generated = []
	gen(size, [], [0,1,2,3,4,5,6,7,8,9], generated)
	return generated

# uses the stuff above to find the solution
def complicated():
	size = 2
	empty = True
	sum = 0
	while True:
		g = generate(size)
		lenG = len(g)
		print("For numbers of size %s, %s results have been found.") % (size, lenG)
		if empty and lenG > 0:
			empty = False
		if not empty and lenG == 0:
			break
		if lenG > 0:
			sum += reduce(lambda x,y: x+y, g)
		size += 1
	print "The result is %s" % sum

# more pythonic and with a bigger complexity solution (brute force)
def naive():
	solutions = []
	for i in range(2,1000000):
		if i == reduce(lambda x,y:x+y, [int(c)**power for c in str(i)]):
			solutions.append(i)
	sum = reduce(lambda x,y:x+y, solutions)
	print "The result is %s" % sum
		
# choose your favorite method :)
# naive has a bigger complexity... but is easier to understand :)
# complicated is much faster!
complicated()
