# -*- coding:utf-8 -*-

# Problem 42

def triangle( limit ):
    n = 0
    i = 1
    while n < limit:
        n += i
        i += 1
        yield n

def word2int( w ):
    return sum([ ord(c)-ord('A')+1 for c in w ])

print "Computing triangle numbers..."
triangle_numbers = {}
for n in triangle( 1000 ):
    triangle_numbers[ n ] = True

print "Reading file..."
n = 0
print "Lookin' for triangle numbers words..."
for w in open('words.txt', 'r').read().replace("\"", "").strip().split(','):
    if triangle_numbers.get( word2int(w), None ):
        n += 1

print "The solution is %s" % n
