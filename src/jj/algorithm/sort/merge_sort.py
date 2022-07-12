# ref: https://www.daleseo.com/sort-merge/

'''
병합 정렬

분할 정복 (Divide and Conquer) 기법과 재귀 알고리즘을 이용한 정렬 알고리즘.
주어진 배열을 원소가 하나 밖에 남지 않을 때까지 계속 반으로 쪼갠 후에 다시 크기순으로 재배열하며 정렬한다.

시간 복잡도

반복적으로 배열을 점점 절반으로 줄이기 때문에 O(logN).
병합할 때, 모든 값들을 비교해야 하므로 O(N)
총 시간 복잡도: O(NlogN)

공간 복잡도
O(N)
'''

def merge_sort(arr):

    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged_arr = []

    l = 0
    r = 0

    while l <len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            merged_arr.append(left_arr[l])
            l += 1
        else:
            merged_arr.append(right_arr[r])
            r += 1

    merged_arr += left_arr[l:]
    merged_arr += right_arr[r:]

    return merged_arr

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(merge_sort(array))