def bin_search_rec(a, b):
	mid = len(a)/2
	if a[mid] == b:
		return True
	elif a[mid] > b and len(a)>1:
		return bin_search_rec(a[:mid],b)
	elif a[mid] < b and len(a)>1:
		return bin_search_rec(a[mid+1:],b)
	else: return False


def bin_search(a,b):
	mi = 0
	ma = len(a)
	while True:
		mid = (ma + mi)/2
		print mid
		if a[mid] == b:
			return True
		elif mid == mi and b<a[mid]:
			return False
		elif mid == ma - 1 and b>a[mid]:
			return False
		elif b < a[mid]:
			ma = mid
		else:
			mi = mid

a = [1,3,5,7,9]
b = 10

print bin_search(a,b)