import queue

class Node:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include

def kp_Best_FS():
    global maxProfit
    global bestset
    temp = n * [0]
    v = Node(-1, 0, 0, 0.0, temp)
    q = queue.PriorityQueue()

    q.put((-v.bound, v))

    while not q.empty():
        u = q.get()[1]

        if u.bound > maxProfit:
            v.level = u.level + 1
            v.weight = u.weight + w[v.level]
            v.profit = u.profit + p[v.level]
            v.bound = compBound(v)
            v.include = u.include + [1]

            if v.weight <= W and v.profit > maxProfit:
                maxProfit = v.profit
                bestset = v.include

            if v.bound > maxProfit:
                q.put((-v.bound, v))

        v = Node(u.level + 1, u.weight, u.profit, u.bound, u.include + [0])
        v.bound = compBound(v)

        if v.bound > maxProfit:
            q.put((-v.bound, v))

def compBound(u):
    if u.weight >= W:
        return 0

    totalWeight = u.weight
    totalProfit = u.profit
    j = u.level + 1

    while j < n and totalWeight + w[j] <= W:
        totalWeight += w[j]
        totalProfit += p[j]
        j += 1

    if j < n:
        totalProfit += (W - totalWeight) * (p[j] / w[j])

    return totalProfit

n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
include = [0] * n
maxProfit = 0
bestset = n * [0]

kp_Best_FS()
print(bestset)
print(maxProfit)
    