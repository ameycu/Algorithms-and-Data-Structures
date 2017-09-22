"""
This code puts even numbers in a list on even indices and odd number of the list on odd indices
"""
l = [5, 2, 8, 6, 11, 23, 18, 1, 9, 10]
l = [1,3,5,7,9,1,3,5,7,9,2,4,6,8,2,4,6,8]
even_ptr = 0
odd_ptr = 1

l_len = len(l)

while even_ptr < l_len and odd_ptr < l_len:
	if l[even_ptr]%2 == 0:
		even_ptr += 2
		continue
	if l[odd_ptr]%2 == 1:
		odd_ptr += 2
		continue
	l[even_ptr], l[odd_ptr] = l[odd_ptr], l[even_ptr]
	even_ptr += 2
	odd_ptr += 2

print l
