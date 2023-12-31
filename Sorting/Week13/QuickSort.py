def quickSort(s, low, high):
    pivotPoint = -1
    if (high > low):
        pivotPoint = partition(s, low, high)
        quickSort(s, low, pivotPoint - 1)
        quickSort(s, pivotPoint + 1, high)
    
def partition(s, low, high):
    pivotItem = s[low]
    j = low
    for i in range(low + 1, high + 1):
        if (s[i] < pivotItem):
            j += 1
            s[i], s[j] = s[j], s[i]
    pivotPoint = j
    s[low], s[pivotPoint] = s[pivotPoint], s[low]
    return pivotPoint

s=[3,5,2,9,10,14,4,8]
quickSort(s,0,7)
print(s)