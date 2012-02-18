# -*- coding:utf-8 -*-	
# http://projecteuler.net/problem=25
# What is the first term in the Fibonacci sequence to contain 1000 
# digits?

# let (fn) be the fibonacci sequence
a = b = 1 # f0 and f1
i = 1 # term index
limit = 10**999 # limit is the first number to have 1000 digits
while b < limit:
	a,b = a+b,a # fibonacci sequence
	i += 1
print "Answer to problem 25 = %s" % i
	
