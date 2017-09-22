"""
This code estimates value of pi using Monte Carlo simulations
"""

import random as r
n_i = 0.0
n = 1000000
for i in range(n):
	x = r.random()
	y = r.random()
	if x**2 + y**2 <= 1:
		n_i += 1
print 4 * n_i/n