#HW01 

#알고리즘 A,B를 한 번에 수행될 수 있도록 하나의 파이썬 프로그램으로 만들어 이름+학번+hw1.py 저장. 
#저장된 프로그램 소스는 n=5,000, 10,000 에 대해 수행되도록 작성

import random
import time

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

n = 5000
#n = 10000
random_list1 = random.sample(range(0, n), n)
random_list2 = random.sample(range(0, n), n)


#Selection Sort (알고리즘 A)
def SelectionSort(my_list):
    list_len = len(my_list)
    for i in range(0, list_len):
        min_idx = i
        for j in range(i + 1, list_len):
            if (my_list[min_idx] > my_list[j]):
                min_idx = j
        swap(my_list, min_idx, i)

#Merge_Sort (알고리즘 B)
def MergeSort(my_list):
    if (len(my_list) <= 1):
        return my_list
    
    mid = len(my_list) // 2
    left_list = my_list[:mid]
    right_list = my_list[mid:]

    left_list = MergeSort(left_list)
    right_list = MergeSort(right_list)

    return Merge(left_list, right_list)

def Merge(left, right):
    result = []
    left_idx = right_idx = 0 
    while (left_idx < len(left) and right_idx < len(right)):
        if (left[left_idx] <= right[right_idx]):
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

SelectionSort(random_list1)
print("Selection Sort:", random_list1)
print("\n")
print("Merge Sort:", MergeSort(random_list2))


