"""
Functions to check if given points form a square
"""

def dist(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def is_sqr(a,b,c,d):
    lengths = sorted([dist(p[0], p[1]) for p in [(a, b), (a, c), (a, d), (b, c), (b, d), (c, d)]])
    return lengths[0]==lengths[1]==lengths[2]==lengths[3]

print is_sqr((0,1),(2,2),(0,2),(2,0))
