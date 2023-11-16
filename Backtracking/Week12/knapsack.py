def kp(i, profit, weight):
    global bestset
    global maxp
    if weight <= W and profit > maxp:
        maxp = profit
        bestset = include[:]

    if promising(i, weight, profit):
        include[i + 1] = 1
        kp(i + 1, profit + p[i + 1], weight + w[i + 1])
        include[i + 1] = 0
        kp(i + 1, profit, weight)

def promising(i, weight, profit):
    global maxp
    if weight >= W:
        return False

    total_weight = weight
    total_profit = profit

    j = i + 1
    while j < n and total_weight + w[j] <= W:
        total_weight += w[j]
        total_profit += p[j]
        j += 1

    if j < n:
        total_profit += (W - total_weight) * (p[j] / w[j])

    return total_profit > maxp

n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
maxp = 0
include = [0] * n
bestset = [0] * n

kp(-1, 0, 0)

print(maxp)
print(bestset)
