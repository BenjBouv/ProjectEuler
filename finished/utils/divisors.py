# -*- coding:utf-8 -*-

from math import ceil, sqrt

def divisors( n ):
    limit = int(ceil(sqrt(n)))
    d = [1]
    for i in xrange( 2, limit ):
        if n % i == 0:
            d.append( i )
            if n / i != i:
                d.append( n / i )
    return d

