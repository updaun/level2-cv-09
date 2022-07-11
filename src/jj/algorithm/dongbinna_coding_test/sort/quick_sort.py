'''
퀵 정렬

기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈.

퀵 정렬은 기준(Pivot)을 설정한 다음 큰 수와 작은 수를 교환한 후, 리스트를 반으로 나누는 방식으로 동작한다.

시간 복잡도

평균 시간 복잡도: O(NlogN)
최선의 경우. 피벗값의 위치가 변경되어 분할이 일어날 때마다 정확히 왼쪽 리스트와 오른쪽 리스트를 절반씩 분활된다면.
데이터가 N개일 때 높이는 약 log2 N.
최악의 경우: O(N^2)

데이터가 무작위로 입력되는 경우 퀵 정렬은 빠르게 동작할 확률이 높다.
하지만 pivot을 가장 왼쪽 데이터로 잡을 때, 이미 데이터가 정렬되어 있는 경우 매우 느리게 동작한다.
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))