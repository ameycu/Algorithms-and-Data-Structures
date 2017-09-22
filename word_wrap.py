"""
This code wraps a string to a new line
"""

s= 'this is a very very very big line in python which i want to word wrap as efficiently as possible'
limit = 15

def wrap_text(s, limit):
	a=s.split()
	count=0
	for i in range(len(a)):
		count = count + len(a[i])
		if count >= limit:
			a[i] = '\n'+a[i]
			count = len(a[i])
	return ' '.join(a)

print wrap_text(s,limit)