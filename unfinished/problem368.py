# -*- coding:utf-8 -*-
from math import fabs

def kempner_filter(n):
	copyN = n
	while copyN > 10:
		if copyN % 10 == 9:
			return False
		copyN /= 10
	if copyN == 9:
		return False
	return True
	
def kempner_sum():
	sum = 0.0
	prec_sum = 100.0
	i = 1
	while (fabs(sum - prec_sum) >= 0.000000000001):
		# print "Prec = %s / Sum = %s" % (prec_sum, sum)
		if kempner_filter(i):
			prec_sum = sum
			sum += 1.0 / i
		i += 1
	return sum
	
print kempner_sum()
