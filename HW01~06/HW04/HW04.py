import random 

#(1) QuickSort
def partition(s, low, high, cmp):
    pivot_item = s[low]
    j = low

    for i in range(low + 1, high + 1):
        cmp[0] += 1
        if s[i] < pivot_item:
            j += 1
            s[i], s[j] = s[j], s[i]

    pivotpoint = j
    s[low], s[pivotpoint] = s[pivotpoint], s[low]
    return pivotpoint

def quickSort(s, low, high, cmp):
    if low < high:
        pivot_index = partition(s, low, high, cmp)
        quickSort(s, low, pivot_index - 1, cmp)
        quickSort(s, pivot_index + 1, high, cmp)

n = 100
#n = 200
#n = 300
#n = 400
random_list = []

for i in range(n):
    random_num = random.randint(0, n)
    random_list.append(random_num)
cmp = [0]

print("(1) QuickSort")
print("정렬 이전:", random_list)
quickSort(random_list, 0, len(random_list) - 1, cmp)
print("정렬 이후:", random_list)
print("데이터 비교 횟수:", cmp[0]) 

print("--------------------------------------------------")

#(2) 큰 정수 곱셈 알고리즘(threshold = 2)
def prod2(u, v, threshold=2):
    if u == 0 or v == 0:
        return 0
    
    n = max(len(str(u)), len(str(v)))
    
    if n <= threshold:
        return u * v
    else:
        m = n // 2
        x = u // 10**m
        y = u % 10**m
        w = v // 10**m
        z = v % 10**m
        
        ac = prod2(x, w, threshold)
        bd = prod2(y, z, threshold)
        ad_bc = prod2(x + y, w + z, threshold) - ac - bd
        
        result = ac * 10**(2 * m) + ad_bc * 10**m + bd
        return result
    
u = 12345678901234567890
v = 98765432109876543210
print("(2) 큰 정수 곱셈 알고리즘(threshold = 2)")
print("곱셈 결과:", prod2(u, v))
