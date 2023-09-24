""" 실습동영상 pfe3에서 17쪽: [실습프로그램] 합병정렬, 27쪽: [실습프로그램] 합병정렬2에 대해
-각 합병정렬 알고리즘 수행에 필요한 추가적인 저장공간(합병정렬 ≒2n, 합병정렬2=n)을  계산할 수 있도록 기능을 추가하여 구현하라. 
    수행 종료 후 필요한 추가적인 저장공간의 개수 및 정렬된 데이터를 출력
-사용한 공간을 반납하는 과정을 고려하여야 함. 
-하나의 프로그램으로 작성
-데이터 = [3,9,10,1,2,16,13,8,7,4,12,6,5,11,14,15]를 이용하여 프로그램을 검증한다.
"""
#Merge_Sort1 저장공간: 2n 
def MergeSort1(my_list):
    if len(my_list) <= 1:
        return my_list, 0 

    mid = len(my_list) // 2

    left_list, left_space = MergeSort1(my_list[:mid])
    right_list, right_space = MergeSort1(my_list[mid:])

    merged_list, merge_space = Merge1(left_list, right_list)
    total_space = left_space + right_space + merge_space 

    return merged_list, total_space

def Merge1(left, right):
    result = []
    left_idx = right_idx = 0
    merge_space = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
        merge_space += 1 

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result, merge_space

def MergeSort2(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort2(arr, low, mid)
        MergeSort2(arr, mid + 1, high)
        return Merge2(arr, low, mid, high)

def Merge2(arr, low, mid, high):
    i = low
    j = mid + 1
    k = low
    U = [0] * (high + 1)

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            U[k] = arr[i]
            i += 1
        else:
            U[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        U[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        U[k] = arr[j]
        j += 1
        k += 1

    for idx in range(low, high + 1):
        arr[idx] = U[idx]
    
    return len(U)

test_list1 = [3,9,10,1,2,16,13,8,7,4,12,6,5,11,14,15]
print("MergeSort1")
test_list1, count1 = MergeSort1(test_list1)
print("추가적인 저장공간:", count1 - len(test_list1)) #반납하는 메모리 고려함. 
print("정렬 결과:", test_list1)

test_list2 = [3,9,10,1,2,16,13,8,7,4,12,6,5,11,14,15]
print("MergeSort2")
count2 = MergeSort2(test_list2, 0, len(test_list2) - 1)
print("추가적인 저장공간:", count2)
print("정렬 결과:", test_list2)