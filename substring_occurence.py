
def count_occur_old(string, char):
	global count
	count += 1
	if len(string)==1:
		if string[0]==char:
			return 1
		else:
			return 0
	else:
		if string[0]==char:
			return count_occur(string[1:],char) + 1
		else:
			return count_occur(string[1:],char)

count = 0
def count_occur(string, s):
	global count
	count += 1
	if len(string)<len(s):
		return 0
	elif len(string)==len(s):
		if string==s:
			return 1
		else:
			return 0
	else:
		if string[:len(s)]==s:
			return count_occur(string[len(s):],s) + 1
		else:
			return count_occur(string[len(s):],s)

co = 0
def count_occur_reoccur(string, s):
	global co
	co += 1
	if len(string)<len(s):
		return 0
	elif len(string)==len(s):
		if string==s:
			return 1
		else:
			return 0
	else:
		if string[:len(s)]==s:
			return count_occur_reoccur(string[1:],s) + 1
		else:
			return count_occur_reoccur(string[1:],s)


search = 'aba'
string = search*8


count_occur(string,search)
print 'without reoccur = ',count

count_occur_reoccur(string,search)
print 'with reoccur = ',co



