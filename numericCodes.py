import math
import numpy as np
import scipy
import scipy.linalg

############## bisection


def f(x):
    return ((0.75*((1+math.cos(x))))**2*math.sin(2*x))/9.8-0.1730861


def bisection(a,b,TOL):
    if not f(a)*f(b)<=0:
        return None
    i = 0
    while((b-a)/2>TOL):
        c = (a+b)/2
        print(i,f'{a:.7f}',
              f'{c:.7f}',
              f'{b:.7f}',
              f'{f(c): .7f}', sep="   ")
        if f(c) == 0:
            break
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        i+=1
    print(i,f'{a:.7f}',
              f'{(a+b)/2:.7f}',
              f'{b:.7f}',
              f'{f(c): .7f}', sep="   ")
    return (a+b)/2


bisections = bisection(0, math.pi*2/9, 0.5*10**-7)
print(f'{bisections:.7f}')
v0 = 0.75*(1+math.cos(bisections))
print(f'{v0:.7f}')
        
############## fixed point
def g(x):
    return math.sqrt(2*x-2)

def fpi(x0,k):
    x = [0 for z in range(k+1)]
    x[0] = x0
    for i in range(k):
        print(i," ",f'{x[i]:.8f}')
        x[i+1] = g(x[i])
    return x[k]

fixed = fpi(1.5,19)

print(fixed)


########## cobweb
def ff(x):
    return 4-x**2
def g(y):
    return (y+1)/4
def cobweb(x0,k):
    x = [0 for z in range(k+1)]
    x[0] = x0
    for i in range(k):
        fi = ff(x[i])
        gi = g(fi)
        print(i+1," ",f'{gi:.6f}')
        x[i+1] = gi
    return x[k]
print(cobweb(1.5,11))
        
##########################linalg
A = np.float64([[2,1,5],[4,4,-4],[1,3,1]])
P,L,U = scipy.linalg.lu(A)
print(P)
print(L)
print(U)