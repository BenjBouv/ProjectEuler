# -*- coding:utf-8 -*-
from math import sqrt

def find_sum_divisors( n ):
    limit = sqrt( n ) + 1
    s = 1
    for i in xrange( 2, limit ):
        if n % i == 0:
            s += i
            if n / i != i:
                s += n / i
    return s

total_sum = 0
alreadyComputed = {}
for i in xrange( 10000 ):
    if alreadyComputed.get( i, None ) == None:
        s = alreadyComputed[i] = find_sum_divisors( i )
        if alreadyComputed.get( s, None ) == None:
            alreadyComputed[s] = find_sum_divisors( s )
        if alreadyComputed[s] == i and s != i:
            print "Amicable pair found: (%s, %s)" % (s, i)
            total_sum += s + i

print "The solution to problem 21 is ", total_sum
