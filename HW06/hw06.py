class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preorder (node):
    if (node is None):
        return
    else:
        print(node.key, end = ' ')
        preorder(node.left)
        preorder(node.right)

def inorder (node):
    if (node is None):
        return
    else:
        inorder(node.left)
        print(node.key, end = ' ')
        inorder(node.right)

def minimum (A, p, i, j):
    minValue = INF
    minK = 0
    for k in range(i, j + 1):
        value = A[i][k - 1] + A[k + 1][j]
        for m in range(i, j + 1):
            value += p[m]
        if (minValue > value):
            minValue = value
            minK = k
    return minValue, minK

def optsearchtree (p):
    n = len(p) - 1
    A = [[-1] * (n + 1) for _ in range(n + 2)]
    R = [[-1] * (n + 1) for _ in range(n + 2)]
    for i in range(1, n + 1):
        A[i][i - 1] = 0
        A[i][i] = p[i]
        R[i][i - 1] = 0
        R[i][i] = i
    A[n + 1][n] = 0
    R[n + 1][n] = 0
    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            A[i][j], R[i][j] = minimum(A, p, i, j)
    return A, R

def tree (R, i, j):
    k = R[i][j]
    if (k == 0):
        return None
    else:
        node = Node(keys[k])
        node.left = tree(R, i, k - 1)
        node.right = tree(R, k + 1, j)
        return node
 
INF = 999
keys = [0, 'A', 'B', 'C', 'D', 'E']
p = [0, 4/16, 3/16, 6/16, 2/16, 1/16]
A, R = optsearchtree(p)
root = tree(R, 1, len(p) - 1)
print("[문제 1번]")
print('inorder:', end = ' ')
inorder(root)
print('\npreorder:', end = ' ')
preorder(root)
print('\n-------------------------------')


def print_matrix(mat):
    for row in mat:
        for item in row:
            print(item, end=" ")
        print()

def dna_alignment(a, b):
    m = len(a)
    n = len(b)

    table = [[0] * (n + 1) for _ in range(m + 1)]
    min_index = [[(0, 0)] * (n + 1) for _ in range(m + 1)]

    for i in range(m, -1, -1):
        table[i][n] = (m - i) * 2

    for j in range(n, -1, -1):
        table[m][j] = (n - j) * 2

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            penalty = 1 if a[i] != b[j] else 0
            options = [
                (table[i + 1][j + 1] + penalty, (i + 1, j + 1)),
                (table[i + 1][j] + 2, (i + 1, j)),
                (table[i][j + 1] + 2, (i, j + 1))
            ]
            table[i][j], min_index[i][j] = min(options)

    return table

a=['C','A','G','A','C','T','A','A']
b=['C','C','G','C','T','A','C']

result = dna_alignment(a, b)
print("[문제 2번]")
print_matrix(result)
print('최소비용:', result[0][0])




