"""
This code creates Tic-Tac-Toe board. It does not check for winner. Just displays board according to player input.
"""

def board():
	return [['.' for i in range(3)] for j in range(3)]

def disp(a):
	for i in range(3):
		for j in range(3):
			print a[i][j]+' ',
		print '\n'

def add(a,c,val):
	a[c[0]][c[1]] = val

a = board()
disp(a)
p1='X'
p2='O'
steps = 0
while steps < 9:
	if steps%2==0:
		x = int(raw_input("Enter x cocrdinate player 1\n"))
		y = int(raw_input("Enter y cocrdinate player 1\n"))
		add(a,(x,y),p1)
	else:
		x = int(raw_input("Enter x cocrdinate player 2\n"))
		y = int(raw_input("Enter y cocrdinate player 2\n"))
		add(a,(x,y),p2)
	steps += 1
	disp(a)