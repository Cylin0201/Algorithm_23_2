#1. BubbleSort
def bubble_sort(S):
    n = len(S)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if (S[j] > S[j + 1]):
                S[j], S[j + 1] = S[j + 1], S[j] #swap

print('#1. BubbleSort')
s = [3, 5, 2, 9, 10, 14, 4, 8]
bubble_sort(s)
print(s)

#2. MergeSort
def merge_sort(n, s):
    h = int(n / 2) 
    m = n - h
    left = s[:h]
    right = s[h:]
    if n > 1:
        merge_sort(h, left)
        merge_sort(m, right)
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

print('#2. MergeSort')
s = [3, 5, 2, 9, 10, 14, 4, 8]
merge_sort(len(s), s)
print(s)