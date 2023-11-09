def queens(i):
    if promising(i):
        if i == n:
            print(col[1:n + 1])
        else:
            for j in range(1, n + 1):
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

n = 10  # 퀸의 수
col = [0] * (n + 1)  # 열마다 퀸의 위치 저장, 1부터 시작

queens(0)
