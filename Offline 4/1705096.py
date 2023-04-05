import numpy as np
import math as ma
import matplotlib.pyplot as plt
xcor = []
ycor = []
ranges = [ .01, .05, .1, .5]
def fun( x, y):
    return (x + 20*y)*ma.sin(x*y)
def euler( prex, prey):
    tempx = prex
    tempy = prey
    for h in ranges:
        prex = tempx
        prey = tempy
        x = []
        l = 0
        u = 10
        #x = np.arange( h , 10 + h, h)
        while u - l > 1e-9:
            l += h
            x.append(l)
        lst1 = []
        lst2 = []
        xcor.append(lst1)
        ycor.append(lst2)
        k = len(xcor) - 1
        xcor[k].append(prex)
        ycor[k].append(prey)
        cnt = 0
        for i in x :
            y = prey + fun( prex, prey)*h
            prey = y
            prex = i
            xcor[k].append(prex)
            ycor[k].append(prey)
            cnt += 1
        #print(prey)

def rk1( prex, prey, a2):
    a1 = 1 - a2
    p1 = (1/2)*(1/a2)
    q11 = p1
    tempx = prex
    tempy = prey
    for h in ranges:
        prex = tempx
        prey = tempy
        x = []
        l = 0
        u = 10
        #x = np.arange( h , 10 + h, h)
        while u - l > 1e-9:
            l += h
            x.append(l)
        lst1 = []
        lst2 = []
        xcor.append(lst1)
        ycor.append(lst2)
        k = len(xcor) - 1
        xcor[k].append(prex)
        ycor[k].append(prey)
        for i in x:
            k1 = fun( prex, prey)
            k2 = fun( prex + p1*h, prey + q11*k1*h)
            y = prey + (a1*k1 + a2*k2)*h
            prex = i
            prey = y
            xcor[k].append(prex)
            ycor[k].append(prey)
        #print(prey)

def rk4( prex, prey):
    tempx = prex
    tempy = prey
    for h in ranges:
        prex = tempx
        prey = tempy
        x = []
        l = 0
        u = 10
        #x = np.arange( h , 10 + h, h)
        while u - l > 1e-9:
            l += h
            x.append(l)
        lst1 = []
        lst2 = []
        xcor.append(lst1)
        ycor.append(lst2)
        k = len(xcor) - 1
        xcor[k].append(prex)
        ycor[k].append(prey)
        for i in x:
            k1 = fun( prex, prey)
            k2 = fun( prex + .5*h, prey + .5*k1*h)
            k3 = fun( prex + .5*h, prey + .5*k2*h)
            k4 = fun( prex + h, prey + k3*h)
            y = prey + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*h
            prey = y
            prex = i
            xcor[k].append(prex)
            ycor[k].append(prey)
        #print(prey)


euler( 0, 4)
rk1( 0, 4, 1/2)
rk1( 0, 4, 1)
rk1( 0, 4, 2/3)
rk4( 0, 4)

k = 1
p = ["Euler", "Heun", "Midpoint", "Ralston", "RK_4"]
q = [".01", ".05", ".1", ".5"]
col = [ "green", "black", "red", "blue", "orange"]
i = 0
j = 0

while i < len(xcor):
    plt.figure(k, figsize=(10,10))
    k += 1
    for j in range( i , i + 4):
        plt.plot( xcor[j], ycor[j], color = col[j%4], label = q[j%4],  linewidth = 3, marker='o', markerfacecolor='yellow', markersize=2)
    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 
    plt.title(p[k - 2])  
    plt.legend()
    i += 4
i = 0
j = 0
while i < 4:
    plt.figure(k, figsize=(10,10))
    k += 1
    j = i
    cnt = 0
    while j < len(xcor):
        plt.plot( xcor[j], ycor[j], color = col[cnt], label = p[cnt],  linewidth = 3, marker='o', markerfacecolor='yellow', markersize=2)
        j += 4
        cnt += 1
    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 
    plt.title(q[i])  
    plt.legend()
    i += 1
plt.show()