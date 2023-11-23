import queue

class Node:
    def __init__(self, level, weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include

def kp_BFS():
    global maxProfit
    global bestset
    q = queue.Queue()

    root = Node(-1, 0, 0, [])
    q.put(root)

    while (not q.empty()):
        u = q.get()
        if (u.level == n - 1):
            continue
        
        v = Node(u.level + 1, u.weight + w[u.level + 1], u.profit + p[u.level + 1], u.include + [1])
        if (v.weight <= W and v.profit > maxProfit):
            maxProfit = v.profit
            bestset = v.include

        if compBound(v) > maxProfit:
            q.put(v)

        v = Node(u.level + 1, u.weight, u.profit, u.include + [0])
        if compBound(v) > maxProfit:
            q.put(v)

def compBound(u):
    if u.weight >= W:
        return 0

    toWeight = u.weight
    toProfit = u.profit
    j = u.level + 1

    while (j < n and toWeight + w[j] <= W):
        toWeight += w[j]
        toProfit += p[j]
        j += 1

    if j < n:
        toProfit += (W - toWeight) * (p[j] / w[j])

    return toProfit

n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
maxProfit = 0
bestset = n * [0]

kp_BFS()
print(bestset)
