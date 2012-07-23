#!/usr/bin/env python

# Solution to Euler's project problem 14

def seq(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

lengths = {}
# took 2.5 seconds with CPython 2.6, 1.5 second with Pypy
def compute_length(n):
    """Solution with memory. Each time a number is processed, the length of its chain is saved, so as to process faster the lengths of paths which contain numbers for which we already have processed paths lengths."""
    global lengths

    if n == 1:
        return 1

    i = seq(n)
    if lengths.get(i, None) != None:
        lengths[ n ] = 1 + lengths[i]
    else:
        lengths[ n ] = 1 + compute_length( i )

    return lengths[n]

def complex():
    maxN = 0
    max = 0
    for n in range(1, 1000000):
        l = compute_length( n )
        if l > max:
            max = l
            maxN = n
    print maxN

complex()

# took 36 seconds with CPython 2.6 on my computer, 7 seconds with Pypy
def chain(n):
    res = n
    while res != 1:
        if res % 2 == 0:
            res /= 2
        else:
            res = res * 3 + 1
        yield res

def naive():
    max = 0
    maxN = 0
    for n in range(1,1000000):
        sequence = [ i for i in chain(n) ]
        #print "Trying for n =", n, ":", sequence
        if len(sequence) > max:
            maxN = n
            max = len(sequence)
    print maxN

"""
complex = [ compute_length(n) for n in range(1, 1000) ]
simple = [ len([i for i in chain(n)]) for n in range(1, 1000) ]
for i in range(1,99):
    if complex[i] - simple[i] > 0:
        print i
        break
"""

#naive()

