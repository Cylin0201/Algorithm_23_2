def promising(i, vcolor, graph, m):
    for j in range(i):
        if graph[i][j] == 1 and vcolor[i] == vcolor[j]:
            return False
    return True

def color(i, vcolor, graph, m):
    if promising(i, vcolor, graph, m):
        if i == n - 1:
            print(vcolor)
        else:
            for c in range(1, m + 1):
                vcolor[i + 1] = c
                color(i + 1, vcolor, graph, m)
                vcolor[i + 1] = 0

n = 4
W = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
vcolor = [0] * n
m = 3

color(-1, vcolor, W, m)
