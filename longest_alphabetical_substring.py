"""
This code is to find longest alphabetical substring in a substring
"""

def substring(s):
	ans = []
	substr = s[0]
	for i in range(1,len(s)):
		if s[i] >= substr[-1]:
			substr += s[i]
		else:
			ans.append(substr)
			substr = s[i]
	ans.append(substr)
	ret = ''
	for i in ans:
		if len(ret) < len(i):
			ret = i
	return ret

def substring_better(s):
	val =''
	substr = s[0]
	for i in range(1,len(s)):
		if s[i] >= substr[-1]:
			substr += s[i]
		else:
			if len(val) < len(substr):
				val = substr
			substr = s[i]
	return val

s = 'azcbobobegghakl'
print substring(s)
print substring_better(s)
