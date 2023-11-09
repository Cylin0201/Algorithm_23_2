print("#1.DFS")
import utility
e={0:[1,2,3], 1:[2,5], 2:[3,4,5,6], 3:[4,6],4:[6,7]}
n=8
a = [ [0 for j in range(0,n)] for i in range(0,n)]
for i in range(0,n-1):
    for j in range(i+1,n):
        if i in e:
            if j in e[i]:
                a[i][j]=1
                a[j][i]=1
utility.printMatrix(a)
visited =n*[0]

def DFS(a,v):
   if (visited[v] == 1):
    return 
   else:
       for j in range(0, n):
           if (a[v][j] == 1 and visited[j] == 0):
               print(j)
               visited[v] = 1
               DFS(a, j)
DFS(a,0)

"""
print("#2.nQueens")
def queens(i):
    if promising(i):
        if i == n:
            print(col[1:n + 1])
        else:
            for j in range(0, n):
                col[i + 1] = j
                queens(i + 1)

def promising(i):
    k = 1
    switch = True
    while (k < i and switch):
        if (col[i] == col[k] or abs(col[i] - col[k]) == i - k):
            switch = False
        k += 1
    return switch

n = 5
col = [0] * (n + 1) 

queens(0)
"""