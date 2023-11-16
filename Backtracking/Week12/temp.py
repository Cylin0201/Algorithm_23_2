def promising(i, weight, total):
    return (weight + total >= W) and (weight == W or weight + w[i] <= W)

def s_s(i, weight, total, include):
    if (promising(i, weight, total)):
        if weight == W:
            print("sol", include)
        else:
            include[i + 1] = 1
            s_s(i + 1, weight + w[i + 1], total - w[i + 1], include )