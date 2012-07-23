#!/usr/bin/env python

string = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

pyramid = [ int(n) for n in ' '.join(string.split('\n')).split(' ') if len(n.strip()) > 0 ]

short = """3
7 4
2 4 6
8 5 9 3"""
#pyramid = [ int(n) for n in ' '.join(short.split('\n')).split(' ') if len(n.strip()) > 0 ]

def line_size(n):
    return n * (n+1) / 2

def search_sum( index, line_nb ):
    if len(pyramid) <= index:
        result = 0
    else:
        #print "pyramid[",index,"]=",pyramid[index], "/", line_nb
        newIndex = index + line_nb
        result = pyramid[ index ] + max( search_sum( newIndex , line_nb+1 ), search_sum( newIndex + 1, line_nb + 1 ) )

    #print result
    return result

def solution():
    return search_sum(0, 1)

print solution()

