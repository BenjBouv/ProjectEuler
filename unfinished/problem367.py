# -*- coding:utf-8 -*-
from random import randint as rand

def random_permute(t):
	i = rand(0,len(t)-1)
	j = rand(0,len(t)-1)
	temp = t[i]
	t[i] = t[j]
	t[j] = temp
	
def is_sorted(t):
	for i in range(1, len(t)):
		if t[i-1] > t[i]:
			return False
	return True

def gen(t, set, generated):
	if len(set) == 0:
		generated.append(t)
	else:
		for n in set:
			copy_t = t[:]
			copy_s = set[:]
			copy_s.remove(n)
			copy_t.append(n)
			gen(copy_t, copy_s, generated)
			
def generatePermutations(t):
	generated = []
	gen([], t, generated)
	return generated

def bozo_sort(t):
	steps = 0
	while not is_sorted(t):
		random_permute(t)
		steps += 1
	return steps

def main():
	base = [1, 2, 3, 4]
	sumSteps = 0
	maxSteps = 100000
	permutations = generatePermutations(base)
	for t in permutations:
		for i in range(maxSteps):
			tab = t[:]
			sumSteps += bozo_sort(tab)
	mean = sumSteps / (len(permutations) * maxSteps)
	print "Expected number of steps : %s" % mean

main()
