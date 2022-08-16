# source: https://www.acmicpc.net/problem/2839

'''
N 킬로그램 배달.
3kg, 5kg 설탕 봉지.

최대한 적은 봉지
만들 수 없다면 -1

3 <= N <= 5,000
'''

n = int(input())

max_5 = n // 5
possible = False

for i in reversed(range(max_5+1)):
    remain = n - i * 5

    if remain % 3 == 0:
        answer = remain // 3 + i

        possible = True
        print(answer)

        break

if not possible:
    print(-1)