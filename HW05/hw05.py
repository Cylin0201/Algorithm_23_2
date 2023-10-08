import numpy as np

def floyd2(W, n):
    P = np.zeros((n, n), dtype=int)
    D = W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (D[i][k] + D[k][j] < D[i][j]):
                    P[i][j] = k
                    D[i][j] = D[i][k] + D[k][j]
    return D, P

inf = 1000
g = [[0, 4, inf, inf, 4],
     [6, 0, inf, inf, inf],
     [1, 2, 0, 1, inf],
     [inf, inf, 4, 0, inf],
     [9, inf, 3, 5, 0]]

d, p = floyd2(g, 5)   
print("[문제1]")
print("v2 -> v4의 최단거리는", d[2 - 1][4 - 1])
print()

def minmult(n, d):
    M = np.zeros((n, n), dtype=int)  
    P = np.zeros((n, n), dtype=int) 

    for diagonal in range(1, n):
        for i in range(n - diagonal):
            j = i + diagonal
            M[i][j] = 999999999999999999
            for k in range(i, j):
                cost = M[i][k] + M[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                if cost < M[i][j]:
                    M[i][j] = cost
                    P[i][j] = k

    return M[0][n-1], P

def order(P, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        k = P[i][j]
        print("(", end="")
        order(P, i, k)
        order(P, k + 1, j)
        print(")", end="")

n = 5
d = [2, 3, 4, 3, 2, 4]      # A1(2 X 3), A2(3 X 4), A3(4 X 3), A4(3 X 2), A5(2 X 4)    

cnt, ord = minmult(n, d)
print("[문제2]")
print("최소 곱셈 횟수:", cnt)
print("최적의 곱셈 순서: ", end="")
order(ord, 0, n - 1)
