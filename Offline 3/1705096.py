import numpy as np
import matplotlib.pyplot as plt
import math as m

eps = 1e-9
plt.style.use('fivethirtyeight') 
plt.figure(figsize=(10,10))
filename = 'input.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
x = []
fx = []
lst = []
p = int(lines[0])
for i in range(p + 1):
    if i == 0:
        continue
    lst = lines[i].split()
    x.append(float(lst[0]))
    fx.append(float(lst[1]))
    lst.clear()
plt.plot( x, fx, color = 'black', label = "curve",  linewidth = 3, marker='o', markerfacecolor='yellow', markersize=5)
plt.plot( [], [], color = 'g', label = "1/3 rule",  linewidth = 5, marker='o', markerfacecolor='yellow')
plt.plot( [], [], color = 'r', label = "3/8 rule",  linewidth = 5, marker='o', markerfacecolor='yellow')
plt.plot( [], [], color = 'b', label = "Trapeziod",  linewidth = 5, marker='o', markerfacecolor='yellow')
i = 1;
rang = []
prev = x[1] - x[0];
start = 0
while i < len(x):
    if abs((x[i] - x[i - 1]) - prev) < eps:
        i += 1
    else:
        prev = x[i] - x[i - 1]
        rang.append(( start, i - 1))
        start = i - 1
        i += 1
rang.append(( start, i - 1))

a = b = c = 0
integral = 0.0
for i in range(len(rang)):
    start = rang[i][0]
    end = rang[i][1]
    if end - start == 1:
        integral += (x[start + 1] - x[start])*((fx[start] + fx[start + 1])/2.00)
        plt.fill_between( [x[start], x[start + 1]], [fx[start], fx[start + 1]], color = 'b', alpha = .5)
        c += 1
    else:
        p = (end - start)%3
        if p == 1:
            p = 4
        while start < end - p:
            integral += (x[start + 3] - x[start])*((fx[start] + 3*fx[start + 1] + 3*fx[start + 2] + fx[start + 3])/8.00)
            plt.fill_between( [x[start], x[start + 1], x[start + 2], x[start + 3]], [fx[start], fx[start + 1], fx[start + 2], fx[start + 3]], color = 'r', alpha = .5)
            start += 3
            a += 1
        while start < end:
            integral += (x[start + 2] - x[start])*((fx[start] + 4*fx[start + 1] + fx[start + 2])/6.00)
            plt.fill_between( [x[start], x[start + 1], x[start + 2]], [fx[start], fx[start + 1], fx[start + 2]], color = 'g', alpha = .5)
            start += 2
            b += 1
        
print("Trapeziod: %d intervals" % c)
print("1/3 rule: %d intervals" % (b*2))
print("3/8 rule: %d intervals" % (a*3))
print()
print("Integral value: %.5f" %integral) 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('Integration')  
plt.legend()
plt.show()        