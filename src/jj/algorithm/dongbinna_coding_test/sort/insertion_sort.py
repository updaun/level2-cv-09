'''
삽입 정렬

데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입.
선택 정렬에 비해 구현 난이도가 높은 편이지만, 선택 정렬에 비해 실행 시간 측면에서 더 효율적인 알고리즘이다.
특히 필요할 때만 위치를 바꾸므로, 데이터가 거의 정렬되어 있을 때 훨씬 효율적이다.

삽입 정렬은 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽입된다는 점이 특징이다.

시간 복잡도

O(N^2)
최선의 경우: O(N)
퀵 정렬과 비교했을 때, 보통은 상입 정렬이 비효율적이나 정렬이 거의 되어 있는 상황에서는 퀵 정렬 알고리즘보다 강력할 수 있다.
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 첫 번째 원소는 그 자체로 정렬되어 있다고 판단.
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]: # 작은 값을 한 칸씩 왼쪽으로 이동.
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 왼쪽 데이터 보다 크다면 멈춘다.
            break

print(array)