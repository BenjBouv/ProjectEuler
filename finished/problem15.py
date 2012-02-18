# -*- coding:utf-8 -*-
# http://projecteuler.net/problem=15
# Starting in the top left corner of a 2x2 grid, there are 6 routes 
# (without backtracking) to the bottom right corner.
# How many routes are there through a 20x20 grid?

# The answer is easy with a recursive function. You have to go on
# 20 squares to the bottom and 20 squares to the right, in the order
# you want.

# To avoid heap explosion by massive recursive calls, let's put a memory
# which saves all the values already computed.
memory = {}
def countRoutes(right, bottom):
	if right == 0 or bottom == 0:
	# if there is no more to go in one of the two directions, we just
	# found one path.
		return 1
	elif (right,bottom) in memory:
	# if we already computed the number of paths for parameters given,
	# just return them
		return memory[right,bottom]
	else:
	# otherwise, the number of paths is the sum of the paths obtained
	# when you go to one of the two directions.
		calc = countRoutes(right-1, bottom) + countRoutes(right, bottom-1)
		memory[right, bottom] = calc
		return calc
		
# n = int(raw_input("Enter the grid's size: "))
n = 20
print countRoutes(n, n)
