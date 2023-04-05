
import numpy as np

filename = 'in1.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    

#n = int(input())
n = int(lines[0].rstrip())
a = np.zeros((n,n))
l = np.zeros((n,n))
u = np.zeros((n,n))
y = np.zeros(n)
x = np.zeros(n)
b = np.zeros(n)
'''
for i in range(n):
    lst = input().split()
    for j in range(n):
        a[i][j] = float(lst[j])
    lst.clear()
for i in range(n):
    b[i] = float(input())
'''
for i in range(n):
    lst = lines[i + 1].rstrip().split()
    for j in range(n):
        a[i][j] = float(lst[j])
    lst.clear()
for i in range(n):
    b[i] = float(lines[i + n + 1].rstrip())
    
for i in range(n):
    l[i][i] = 1
    if i == 0:
        u[0][0] = a[0][0]
        for j in range( 1, n):
            u[0][j] = a[0][j]
            l[j][0] = a[j][0]/u[0][0]
    else:
        for j in range( i, n):
            sum = 0
            for k in range(i):
                sum += l[i][k]*u[k][j]
            u[i][j] = a[i][j] - sum
        for j in range( i + 1, n):
            sum = 0
            for k in range( 0, i):
                sum += l[j][k]*u[k][i]
            l[j][i] = (a[j][i] - sum)/u[i][i]
#print(np.around(l, decimals = 3))
#print()
#print(np.around(u, decimals = 3))
#print()
filename = 'out1.txt'
with open( filename, 'w') as file_object:
    for i in range(n):
        for j in range(n):
            file_object.write( "%.4f" % round(l[i][j], 4) + " ")
        file_object.write("\n")
    file_object.write("\n")
with open( filename, 'a') as file_object:
    for i in range(n):
        for j in range(n):
            file_object.write( "%.4f" % round(u[i][j], 4) + " ")
        file_object.write("\n")
    file_object.write("\n")
ok1 = True
for i in range(n):
    ok = False
    for j in range(n):
        if u[i][j] != 0: 
            ok = True
    if ok == False:
        #print("No unique solution")
        with open( filename, 'a') as file_object:
            file_object.write("No unique solution")
            exit()
        ok1 = False

for k in range(n - 1):
    if ok1 == False:
        break
    for i in range( k + 1, n):
        factor = l[i][k]/l[k][k]
        for j in range( k + 1, n):
            l[i][j] -= factor*l[k][j]
        b[i] -= factor*b[k]
y[n - 1] = b[n - 1]/l[n - 1][n - 1]
for i in range( n - 2, -1, -1):
    if ok1 == False:
        break
    sum = b[i]
    for j in range( i + 1, n):
        sum -= l[i][j]*y[j]
    y[i] = sum/l[i][i]
'''
for i in range(n):
    if ok1 == False:
        break
    print(round(y[i], 3))
print() '''
if ok1 != False:
    with open( filename, 'a') as file_object:
        for i in range(n):
            file_object.write( "%.4f" % round(y[i], 4))
            file_object.write("\n")
        file_object.write("\n")
for k in range(n - 1):
    if ok1 == False:
        break
    for i in range( k + 1, n):
        factor = u[i][k]/u[k][k]
        for j in range( k + 1, n):
            u[i][j] -= factor*u[k][j]
        y[i] -= factor*y[k]
x[n - 1] = y[n - 1]/u[n - 1][n - 1]
for i in range( n - 2, -1, -1):
    if ok1 == False:
        break
    sum = y[i]
    for j in range( i + 1, n):
        sum -= u[i][j]*x[j]
    x[i] = sum/u[i][i]
    '''
for i in range(n):
    if ok1 == False:
        break
    print(round(x[i], 3))
    '''
if ok1 != False:
    with open( filename, 'a') as file_object:
        for i in range(n):
            file_object.write( "%.4f" % round(x[i], 4))
            file_object.write("\n")

    


