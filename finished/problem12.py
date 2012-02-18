# -*- using:utf-8 -*-
# http://projecteuler.net/problem=12
# What is the value of the first triangle number to have over five 
# hundred divisors?

import math

class TriangleNumberFactory:
	def __init__(this):
		this.n = 1
		this.number = 0
	
	# Computes the next triangle number factory.
	def next(this):
		this.number += this.n
		this.n += 1
		return this.number
		
# Counts the number of divisors of n.
def countDivisors(n):
	numberOfDivisors = 0
	limit = math.sqrt(n)
	max = 0
	i = 1
	while i <= limit:
		if n % i == 0:
			numberOfDivisors += 1
			if n / i != i:
				numberOfDivisors += 1
		i += 1
	return numberOfDivisors

# Function to test the above function.
def testCountDivisors():
	numbers = [1, 3, 6, 10, 15, 21, 25, 28]
	expected = [1, 2, 4, 4, 4, 4, 3, 6]
	for i in range(len(numbers)):
		count = countDivisors(numbers[i])
		if(expected[i] != count):
			print "Error for n = %s. Expected : %s / Count divisors : %s" %(numbers[i], expected[i], count)
		assert(expected[i] == count)

testCountDivisors()

t = TriangleNumberFactory()
n = t.next()
while countDivisors(n) < 500:
	n = t.next()

print "The solution is : %s " % n
