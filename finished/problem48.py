# -*- coding:utf-8 -*-

# Euler's project : problem 48
"""Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000."""

numberOfDigits = 10
limit = 1000

modulo = 10**numberOfDigits

def modulopower(a, n, mod):
    if n == 1:
        return a % mod
    elif n % 2 == 0:
        return ( modulopower( a, n/2, mod )**2 ) % mod
    else:
        return ( modulopower( a, n/2, mod )**2 * ( a % mod ) ) % mod

daSum = 0
for i in range(1,limit):
    daSum = ( daSum + modulopower( i, i, modulo ) ) % modulo
print daSum
