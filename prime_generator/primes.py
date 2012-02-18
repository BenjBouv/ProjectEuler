# -*- coding:utf-8 -*-
# Computes primes numbers with simple algorithm : checks all the
# potentials prime divisors less than square root(n). The only values to
# check and greater than 3 have the form 6n-1 or 6n+1, for n non zero
# integer.
from math import sqrt

stepNumber = 150000 # computes primes number less than 6 * stepNumber
namePrimesFile = "primes.txt"
primes = [2, 3]

n1 = -1
n2 = +1

def check_is_prime(n):
	limit = sqrt(n)
	for p in primes:
		if n % p == 0:
			return False
		if p > limit:
			return True
	return True

def search_primes(attempts):
	global n1, n2
	while attempts > 0:
		attempts -= 1
		n1 += 6
		n2 += 6
		if check_is_prime(n1):
			primes.append(n1)
		if check_is_prime(n2):
			primes.append(n2)
	
def save():
	file = open(namePrimesFile, "w+")
	for p in primes:
		file.write("%s\n" % p)
	file.close()

search_primes(stepNumber)
save()
