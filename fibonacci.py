"""
This code contains different ways fibonacci series can be implemented
"""
import time

def fibonacci_recur(n):
    """
    This function has exponential complexity
    """
    if n == 0 or n == 1:
        return n
    else: 
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)


def fibonacci_list(n):
    """
    This function has linear complexity
    """
    if n == 0 or n == 1:
        return n
    f = [0,1]
    for i in range(n):
        if n == len(f)-1:
            return f[-1]
        else:
            f.append(f[-1]+f[-2])


f = [0,1]
def fibonacci_global_list(n):
    """
    This function has linear complexity
    """
    global f
    if n == 0 or n == 1:
        return n
    while n > len(f)-1:
        f.append(f[-1]+f[-2])
    return f[-1]


n = 30

t = time.time()
for i in xrange(n): fibonacci_recur(i)
print time.time() - t

n *= 50
t = time.time()
for i in xrange(n): fibonacci_list(i)
print time.time() - t

n *= 50
t = time.time()
for i in xrange(n): fibonacci_global_list(i)
print time.time() - t
