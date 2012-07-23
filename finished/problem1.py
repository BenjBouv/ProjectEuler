#!/usr/bin/env python
# Euler's first problem. Uses a python generator instead of a simple loop: KIHN (Keep It Hard, Nerdy)

def three_or_five( limit ):
    i = 1
    while i < limit:
        if i % 3 == 0 or i % 5 == 0:
            yield i
        else:
            yield 0
        i += 1

print "Result is", sum( three_or_five(1000) )

