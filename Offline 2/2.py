
import numpy as np

#cnt = 0
lst2 = []
'''
while True:
    try:
        lst1 = input().split()
        if len(lst1) == 0:
            break
        lst2.append([])
        for i in range(len(lst1)):
            lst2[len(lst2) - 1].append(lst1[i])
        if cnt == 0:
            k = len(lst1)
            cnt += 1
        lst1.clear()
    except EOFError:
        break
'''
filename = 'in2.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

#n = len(lst2)
for i in range( len(lines)):
    lst1 = lines[i].rstrip().split()
    lst2.append([])
    for j in range(len(lst1)):
        lst2[len(lst2) - 1].append(lst1[j])
    if i == 0:
        k = len(lst1)
    lst1.clear()
n = len(lst2)
rows = 0
cols = 0
cols = k + n -1
rows = n
x = np.zeros(( rows, cols))
table = np.zeros((rows, cols + 1))
val = np.zeros(rows)
theta = np.zeros(rows)
basic = np.zeros(rows)
ans = np.zeros(cols)

for i in range(rows):
    for j in range(cols):
        if i == 0:
            if j >= len(lst2[i]):
                break
            x[i][j] = -float(lst2[i][j])
        else:
            if j == len(lst2[i]) - 1:
                val[i] = float(lst2[i][j])
            elif j < len(lst2[i]) - 1:
                x[i][j] = float(lst2[i][j])
            else:
                break
p = k
for i in range( 1, rows):
    x[i][p] = 1.0
    p += 1
p = k
for i in range( 1, rows):
    basic[i] = p
    p += 1
pivotr = 0
pivotc = 0
while True:
    for i in range(rows):
        for j in range(cols):
            table[i][j] = x[i][j]
        table[i][j + 1] = val[i]
    for i in range(rows):
        for j in range(cols + 1):
            print("%.2f" % round( table[i][j], 2), end = " ")
        print()
    print()
    minn  = 100000000
    pivotr = -1
    pivotc = -1
    for i in range(cols):
        if x[0][i] < minn:
            pivotc = i
            minn = x[0][i]
    if minn >= 0.0:
        break
    if pivotc == -1:
        break
    for i in range( 1, rows):
        if x[i][pivotc] == 0:
            theta[i] =  1000000000
        else:
            theta[i] = val[i]/x[i][pivotc]
    minn  = 100000000
    for i in range( 1, rows):
        if theta[i] < minn and theta[i] > 0:
            minn = theta[i]
            pivotr = i
    if pivotr == -1:
        break
    pivot = x[pivotr][pivotc]
    basic[pivotr] = pivotc
    for i in range(cols):
        x[pivotr][i] = x[pivotr][i]/pivot 
    val[pivotr] = val[pivotr]/pivot
    for i in range(rows):
        if i == pivotr :
            continue
        fact = x[i][pivotc]
        for j in range(cols):
            x[i][j] -= fact*1.00*x[pivotr][j]
        val[i] -= fact*val[pivotr]
print("%.2f" % round( val[0], 2))
for i in range( 1, rows):
    ans[int(basic[i])] = val[i]
for i in range(k):
    print("%.2f" % round( ans[i], 2), end = " ")

        
    
