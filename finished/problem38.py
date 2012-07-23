#!/usr/bin/env python

# Solution to problem 38

def weak_is_pandigital(n):
    """Fast way to determine if a number n is pandigital: sum of its digits must be 45. It's a necessary but not a
    sufficient condition."""
    return sum([ int(k) for k in str(n) ]) == 45

def strong_is_pandigital(n):
    """Strict check that a number n is pandigital."""
    digits = {}
    for a in [ int(k) for k in str(n) ]:
        if digits.get( a, None ) != None:
            return False
        else:
            digits[a] = True
    return True

def is_pandigital(n):
    """Efficient way to check whether a number n is pandigital: it fulfills the weak and strong conditions."""
    return weak_is_pandigital(n) and strong_is_pandigital(n)

def create_concat( p, n ):
    """Creates the concatenation of p,2p,3p,...,np"""
    return "".join( [str(p*i) for i in range(1,n+1)] )

def try_n( p ):
    """For a precise value p, tries all values of n and check if the concatenation is pandigital, until we get more than 10 numbers"""
    best = None
    for n in range(1, 10):
        concat = create_concat( p, n )
        if len(concat) > 9:
            return best
        if is_pandigital(int(concat)):
            best = int(concat)
    return best

best = 0
# Limit is 10000: for n == 2, 1000020000 has more than 10 digits.
for p in range(1, 10000):
    sol = try_n(p)
    if sol != None:
        if sol > best:
            best = sol
            print sol

"""
print is_pandigital(192384576)
print is_pandigital(192384477)
print is_pandigital(192384577)
print create_concat( 192, 3 )
"""
