# -*- coding:utf-8 -*-

from utils.primes import *

primes_until( 100000 )

def compute( a, b, n ):
    return n * n + a * n + b

def test_formula( a, b ):
    n = 0
    c = compute( a, b, n )
    while is_prime( c ):
        n += 1
        c = compute( a, b, n )
    return n

def test_and_remember( a, b, amax, bmax, tmax ):
    t = test_formula( a, b )
    if t > tmax:
        tmax, amax, bmax = t, a, b
    return tmax, amax, bmax

tmax = 0
amax = 0
bmax = 0

for p in primes:
    if p > 1000:
        break

    b = p
    for halfA in xrange(500):
        a = 2 * halfA + 1
        tmax, amax, bmax = test_and_remember( a, b, amax, bmax, tmax )
        tmax, amax, bmax = test_and_remember( -a, b, amax, bmax, tmax )
        tmax, amax, bmax = test_and_remember( -a, -b, amax, bmax, tmax )
        tmax, amax, bmax = test_and_remember( a, -b, amax, bmax, tmax )

print "Solution to problem 27 is %s (which is the product of coefficients %s and %s, that produce %s primes)" % ( amax * bmax, amax, bmax, tmax )

