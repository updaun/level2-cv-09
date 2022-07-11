'''
선택 정렬

가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정 반복.
매번 가장 작은 것을 '선택'한다는 의미에서 선택 정렬 알고리즘이라고 한다.

시간 복잡도

N-1번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다. 또한, 매번 가장 작은 수를 찾기 위한 비교 연산이 필요하다.
연산 횟수는 N + (N - 1) + (N - 2) + ... + 2로 볼 수 있다. 근사치로 N X (N + 1) / 2 번의 연산을 수행한다고 가정할 수 있다.
=> (N^2 + N) / 2로 O(N^2)이라고 표현할 수 있다.
'''

array = [7, 5, 9, 0, 3, 1 , 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스를 저장할 변수

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i]

print(array)