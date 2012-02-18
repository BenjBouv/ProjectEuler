# -*- coding:utf-8 -*-
# http://projecteuler.net/problem=20
# Find the sum of the digits in the number 100!

# Returns the sum of digits of the integer n.
def sumOfDigits(n):
	sum = 0
	while n >= 10:
		sum += n % 10 # adds last number
		n /= 10
	sum += n # adds the last number a last time (n == n%10 since n < 10)
	return sum
	
# Computes n!
def factorial(n):
	f = 1
	while n > 1:
		f *= n
		n -= 1
	return f
		
print "Sum of digits is %s." % sumOfDigits(factorial(100))

