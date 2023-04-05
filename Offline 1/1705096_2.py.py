import math as ma
import numpy as np
import matplotlib.pyplot as plt

def fM( fnc, xi, xu, es, maxi):
    if fnc(xi)*fnc(xu) >= 0:
        return None
    i = 0
    ea = 1.1*es
    xro = 0
    while ea > es and i < maxi:
        xr = xu - (fnc(xu)*(xi - xu))/(fnc(xi) - fnc(xu))
        i += 1
        if not(i == 1 or xr == 0):
            ea = abs((xr - xro)/xr)*100
        test = fnc(xi)*fnc(xr)
        if test == 0:
            ea = 0.0
        elif test < 0:
            xu = xr
            xro = xr
        else:
            xi = xr
            xro = xr
    return (xr,i)
        
def sM( fnc, xi, xj, es, maxi):
    if fnc(xi)*fnc(xj) >= 0:
        return None
    xh = 0
    ea = 1.1*es
    i = 0
    while ea > es and i < maxi:
        i += 1
        xh = xi
        xi = xj
        xj = xi - ((xh - xi)/(fnc(xh) - fnc(xi)))*fnc(xi)
        if not(i == 1 or xj == 0):
            ea = abs((xj - xi)/xj)*100
    return (xj,i)    
            

plt.style.use('fivethirtyeight') 
fig = plt.figure(figsize=(20,30))
lst = []
x = np.arange( -.5, .5, .1)
for a in x:
    lst.append((a/(1 - a))*(ma.sqrt(6/(2 + a))) - .05)
y = np.array(lst)
lst.clear()
plt.plot( x, y, label = "Graphical Method", linewidth = 4, marker = 'o', markerfacecolor = 'black', markersize = '10')
plt.legend()
plt.show()
f = lambda a : (a/(1 - a))*(ma.sqrt(6/(2 + a))) - .05
print(fM(  f,-.5, .5, .5, 1000000))
print( sM( f, -.5, .5, .5, 1000000))