inf = 1000
w = [[0, 7, 4, 6, 1], [inf, 0, inf, inf, inf], [inf, 2, 0, 5, inf], [inf, 3, inf, 0, inf], [inf, inf, inf, 1, 0]]
n = 5
f = set()
touch = n * [0]
length = n * [0]

for i in range(1, n):
    length[i] = w[0][i]

for i in range(1, n):
    min_dist = inf
    for j in range(1, n):
        if 0 <= length[j] < min_dist and j not in f:
            vnear = j
            min_dist = length[j]
    f.add(vnear)

    for j in range(1, n):
        if length[vnear] + w[vnear][j] < length[j]:
            length[j] = length[vnear] + w[vnear][j]
            touch[j] = vnear

print(touch[1:])
print(f)
print("최단거리:", length)
