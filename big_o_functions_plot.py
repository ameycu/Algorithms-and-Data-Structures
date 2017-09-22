import pylab as p
import math as m

x = range(900,1014,10)
p.figure(1)

def plot(y,n):
	p.plot(x,y,label=n)

plot(x,'1')
plot([i**(4) for i in x],'2')
plot([i**(-1) for i in x],'3')
plot([i*m.log(i,2) for i in x],'4')
plot([1 for i in x],'5')
plot([i**(1/(m.log(i,2)**0.5)) for i in x],'6')
plot([m.log(m.factorial(i)) for i in x],'7')
plot([2**(i+10) for i in x],'8')
plot([i**(1/(m.log(i,2))) for i in x],'9')
plot([m.log((m.log(i)**2),2) for i in x],'10')
plot([(i+1000)**2 for i in x],'11')
plot([2**(i+m.log(i,2)) for i in x],'12')
plot([(m.log(i,2))**2 for i in x],'13')
plot([(m.log(i*m.log(i,2),2))**2 for i in x],'14')
plot([13**(m.log(i,2)) for i in x],'15')
plot([m.log(m.log(i,2),2) for i in x],'16')
plot([i*i for i in x],'17')
plot([(1.01)**i for i in x],'18')
plot([i**(m.log(i,2)) for i in x],'19')
plot([2**i for i in x],'20')

p.grid()
p.legend(loc='best')
p.show()

# 3 5 9 16 10 6 13 14 1 7 4 18 17 11 15 2 19 20 12 8