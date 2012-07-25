# -*- coding:utf-8 -*-
from utils.primes import primes, primes_until

# Euler's project: problem 50
""" Which prime, below one-million, can be written as the sum of the 
most consecutive primes?"""

LIMIT = 1000000
primes_until( LIMIT ) # compute primes until LIMIT

# only considers suites beginning from 2: incomplete solutions.
def from_beginning():
    global LIMIT
    sum = 0
    i = 0
    while sum < LIMIT:
        sum += primes[i]
        i += 1
        if sum in primes:
            print sum

# Generator used for the next solution, which makes all the sums and yields them
def extender( init, max ):
    t = [ primes[init] ]
    i = init+1
    while i < max:
        t.append( primes[ i ] )

        daSum = sum(t)
        daLen = len(t)
        if daSum in primes:
            yield ( daSum, daLen )
        i += 1

def naive():
# works "fast" until LIMIT = 10000
    sums = []
    size = len(primes)

    max_len = 0
    result = 0
    for i in range( size ):
        new_couples = [a for a in extender(i, size)]
        for c in new_couples:
            if c[1] > max_len:
                result = c[0]
                max_len = c[1]

    print result

# Solved in 4 min 54 seconds (PyPy on my laptop)...
# The idea: from already existing primes number, try to find a suite of consecutives
# primes whose sum is equal to the prime => less tries to give, as we only test the suites
# whose sum is a prime!

# The program prints a line, containing the sum then the length, each time we find a better solution
# The solution to the problem is hence the last written sum

maxL = 0
maxP = 0

"""
limit = 0
for p in primes:
    limit += 1
    if p == 953:
        break
"""

limit = len(primes)
for p in range(limit):
    aim = primes[p]
    i = init = 0
    while init < limit:
        sum = 0
        init = i
        while i < limit and sum < aim:
            sum += primes[i]
            i += 1
        if sum == aim:
            if i - init > maxL:
                maxL = i - init
                maxP = aim
                print aim, maxL
            break
        i = init+1




