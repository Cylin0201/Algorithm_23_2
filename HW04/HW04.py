"""
(1) 12쪽: [실습프로그램] 빠른정렬 프로그램을 다음의 내용을 포함하도록 python으로 완성하라. 문제의 크기, 즉 데이터의 개수를 n으로 표시한다. 
n=100,200,300,400 이 된다. 각 n에 대해서 다음을 구현한다. 정렬할 데이터를 100 set를 생성한다. 데이터는 0부터 n까지의 random number 정수로 구성되고, 중복이 허락된다. 
100개의 데이터 set를 quick sort로 정렬할 때 평균 데이터 비교 횟수 (if (s[i]<pivotItem )를 구하라. 
최종적으로 가로축에 n, 세로축에 평균 데이터 비교 횟수를 표시하는 그래프를 생성하여 그 점들을 이어주는 선에 대해 설명하라.

(2) 23쪽: [실습프로그램] 큰 정수 곱셈 알고리즘을 python으로 완성하라. 여기서 threshold를 2로 설정한다.
"""
import random 

#(1) QuickSort
def partition(s, low, high):
    pivot_index = low
    s_p = low + 1
    e_p = high

    while s_p <= e_p:
        while s_p <= e_p and s[s_p] <= s[pivot_index]:
            s_p += 1
        while s[e_p] >= s[pivot_index] and e_p >= s_p:
            e_p -= 1
        if e_p < s_p:
            break
        s[s_p], s[e_p] = s[e_p], s[s_p]

    s[e_p], s[pivot_index] = s[pivot_index], s[e_p]

    return e_p

def quickSort(s, low, high):
    if low < high:
        pivot = partition(s, low, high)
        quickSort(s, low, pivot - 1)
        quickSort(s, pivot + 1, high)


n = 100
#n = 200
#n = 300
#n = 400
random_list = []

for i in range(n):
    random_num = random.randint(0, n)  # 0부터 n까지의 랜덤 정수 생성
    random_list.append(random_num)

print(random_list)
quickSort(random_list, 0, len(random_list) - 1)
print(random_list)
