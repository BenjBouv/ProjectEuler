# -*- coding:utf-8 -*-
# Computes primes numbers with simple algorithm : checks all the
# potentials prime divisors less than square root(n). The only values to
# check and greater than 3 have the form 6n-1 or 6n+1, for n non zero
# integer.
from math import sqrt, ceil

namePrimesFile = "primes.txt"

primes = [2, 3]
primes_map = {}
limit_processed = 3
n1 = -1
n2 = +1

def check_is_prime(n):
    limit = sqrt(n)
    result = True
    for p in primes:
        if n % p == 0:
            result = False
            break
        if p > limit:
            break
    return result

def seek_primes(attempts):
    global n1, n2, limit_processed
    while attempts > 0:

        while n2 <= limit_processed and n1 <= limit_processed:
            attempts -= 1
            n1 += 6
            n2 += 6

        if check_is_prime(n1):
            primes.append(n1)
        if check_is_prime(n2):
            primes.append(n2)

        limit_processed = n2

def primes_until( limit ):
    global primes_map
    seek_primes( 1 + limit / 6 )
    for p in primes:
        primes_map[ p ] = True

def is_prime( n ):
    return primes_map.get( n, None ) != None

def save():
    file = open(namePrimesFile, "w+")
    for p in primes:
        file.write("%s\n" % p)
    file.close()

def load():
    primes = []
    file = open(namePrimesFile, "r")
    for l in f:
        primes.append( int( l.strip() ) )
        primes_map[ p ] = True
    f.close()

def main():
    """When used as the primary program, computes prime numbers until the program is stopped by Ctrl+C"""
    try:
        while True:
            seek_primes( 5000 )
            print primes[ len(primes)-1 ]
    except KeyboardInterrupt:
        print "Ctrl C caught, gonna save the primes in the file..."
        save()

if __name__ == "__main__":
    main()
