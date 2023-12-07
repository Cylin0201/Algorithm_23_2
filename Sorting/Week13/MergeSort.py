def mergeSort(n, s):
    h = int(n / 2) 
    m = n - h
    left = s[:h]
    right = s[h:]
    if n > 1:
        mergeSort(h, left)
        mergeSort(m, right)
        merge(h, m, left, right, s)

def merge(h, m, u:list, v:list, s):
    i = j = k = 0
    while i < h and j < m:
        if u[i] < v[j]:
            s[k] = u[i]
            i += 1
        else:
            s[k] = v[j]
            j += 1
        k += 1

    while i < h:
        s[k] = u[i]
        i += 1
        k += 1

    while j < m:
        s[k] = v[j]
        j += 1
        k += 1


s = [3, 5, 2, 9, 10, 14, 4, 8]
mergeSort(len(s), s)
print(s)
