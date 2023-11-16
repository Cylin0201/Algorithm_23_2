def promising(i, weight, total):
    return (weight + total >= W) and (weight == W or weight + w[i] <= W)

def s_s(i, weight, total, include):
    if promising(i, weight, total):
        if weight == W:
            print("sol", include)
        else:
            include[i + 1] = 1
            s_s(i + 1, weight + w[i + 1], total - w[i + 1], include)
            include[i + 1] = 0
            s_s(i + 1, weight, total - w[i + 1], include)

n = 4
w = [1, 2, 4, 6]
W = 6
print("Items =", w, "W =", W)
include = [0] * n
total = sum(w)

s_s(-1, 0, total, include)

"""
n = 100
w = [i for i in range(1, 101)]
W = 365
print("Items =", w, "W =")
include = [0] * n
total = sum(w)
s_s(-1, 0, total, include)
"""