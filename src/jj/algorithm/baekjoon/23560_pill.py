# source: https://www.acmicpc.net/problem/23560
# ref: https://dong-gas.tistory.com/36

'''
N일 동안 약 먹기
3N개 일렬로 (아침, 점심, 저녁)
앞에 있는 것과 뒤에 있는 것만 뜯어서 먹을 수 있다.

아침 약 == 저녁 약
'''

# dynamic programming
n = int(input())

# a = 2 
# b = 1

# for _ in range(n-1):
#     tmp_a = a
#     a = 2*a + 2*b
#     b = b + tmp_a

# print(a)

a = 2

for _ in range(n-1):
    a *= 3

print(a)
