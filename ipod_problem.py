"""
Ipod problem
Fastest way to go from one song to other 
with the number of times button has to be pressed
"""

a = list('abcdefghijklmnopqrstuvwxyz')

def fun(a,x,y):
	var = 0
	m = len(a)
	start = a.index(x)
	while True:
		if a[(start+var)%m] == y: return ('up', var)
		if a[(start-var)%m] == y: return ('down', var)
		var += 1

print fun(a,'a','z')