
import math as ma
import numpy as np
import matplotlib.pyplot as plt

def fnc( x, n):
    ans = 0.0
    for i in range( 1, n + 1):
        if i%2 == 1 :
            ans += (x**i)/i
        else:
            ans -= (x**i)/i
    return ans
plt.style.use('fivethirtyeight') 
fig = plt.figure(figsize=(20,30))
plt1 = fig.add_subplot(221) 
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
#Q-a
x = int(input("x : "))
n = int(input("n : "))
print(fnc( x, n))
#Q-a
plt.xlim(-1,55)
#Q-b
x = np.arange( 1, -1, -0.1)
y = [np.log(1 + x)]
plt1.plot( x, y[0], label = str(0), linewidth = 4, marker = 'o', markerfacecolor = 'black', markersize = '10')
#Q-b
#Q-c
num_of_terms = [ 1, 3, 5, 20, 50]
lst1 = []
for n in num_of_terms:
    for z in x:
        lst1.append(fnc( z, n))
    y.append(np.array(lst1))
    lst1.clear()
for i in range( 1, len(y)):
    plt2.plot( x, y[i], label = str(i), linewidth = 4, marker = 'o', markerfacecolor = 'black', markersize = '10')
#Q-c
#Q-d
prev_a = 0.5
curr_a = 0.0

for x in range(2,51):
    curr_a = fnc( .5, x)
    error = (abs((curr_a - prev_a))*100)/curr_a
    prev_a = curr_a
    lst1.append(error)
y.clear()
x = np.arange( 2, 51, 1)
y.append(np.array(lst1))
plt3.plot( x, y[0], label = str(6), linewidth = 4, marker = 'o', markerfacecolor = 'black', markersize = '10')
#Q-d
fig.subplots_adjust(hspace=.5,wspace=0.5) 
plt1.legend()
plt2.legend()
plt3.legend()
plt.show()
