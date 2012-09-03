# -*- coding:utf-8 -*-

from utils.primes import primes, primes_until

def make_circular( initial ):
    return "".join([ initial[1:len(initial)], initial[0] ])

def circulars( n ):
    initial = str(n)
    result = make_circular( initial )
    yield int(result)
    while result != initial:
        result = make_circular( result )
        yield int(result)


"""
print [c for c in circulars(154)]
print [c for c in circulars(11)]
print [c for c in circulars(190)]
"""

def monotone( result, possibles, nb_digits, results ):
    if nb_digits == 0:
        results.append( result )
    else:
        cPossibles = possibles[:]
        for c in possibles:
            monotone( result * 10 + int(c), cPossibles, nb_digits - 1, results )
            cPossibles.remove( c )

def monotone_call( LIMIT ):
    possibles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    results = []
    #monotone( "", possibles, 3, results )
    monotone( 0, possibles, len(str(LIMIT))-1, results )
    return results

LIMIT = 1000000
print "Compute primes until", LIMIT,"..."
primes_until(LIMIT)

primes_map = {}
for p in primes:
    primes_map[ p ] = True

print "Creates testable numbers..."
#monotones = monotone_call( LIMIT )
#testables = [ m for m in monotones if m in primes ]
#testables = [ p for p in primes if p < LIMIT ]
testables = [ p for p in range(LIMIT) ]

testables_map = {}
for p in testables:
    testables_map[ p ] = True

print "Searches for circulars..."
#print testables

"""
count = 0
i = 0
for t in testables:
    if i == 1000:
        i = 0
        print "Testing", t
    i += 1

    its_circulars = [ c for c in circulars(t) ]
    its_circulars_primes = [ c for c in its_circulars if c in primes ]
    if len( its_circulars_primes ) == len( its_circulars ):
        count += len(its_circulars) # adds the number of unique circular permutation
print count
"""

compteur = 0
def fast_circulars( n, testables ):
    global compteur
    if compteur == 100:
        compteur = 0
        #print n
    compteur += 1

    its_circulars = []

    initial = str(n)
    inp = initial
    result = ""

    while result != initial:
        result = make_circular( inp )
        its_circulars.append( int(result) )
        inp = result

    circularPrime = True
    for c in its_circulars:
        if primes_map.get(c,None) == None:
            circularPrime = False
            break

    for c in its_circulars:
        testables_map[ c ] = False

    if not circularPrime:
        return 0

    return len(its_circulars)

count = 0
for i in range(len(testables)):
    if testables_map[ testables[i] ]:
        count += fast_circulars( testables[i], testables )

print count
