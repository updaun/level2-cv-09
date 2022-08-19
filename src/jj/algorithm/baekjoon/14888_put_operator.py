# source: https://www.acmicpc.net/problem/14888

'''
N개의 수로 이루어진 수열 A_1, ..., A_N.
또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자.

연산자의 종류: +, -, x, /

식의 계산은 앞에서부터 진행 (연산자 우선 순위 무시)
나눗셈은 몫만 취한다.
음수를 양수로 나눌 때는 C++14의 기준. == 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것.
'''

'''
만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성.
'''

'''
입력
첫째 줄: 수의 개수 (2 <= N <= 11)
둘째 줄: A_1, ... A_N (1 <= A_i <= 100)
셋째 줄: 합이 N-1인 4개의 정수. 차례대로 +, -, x, /의 개수

출력
첫째 줄에 만들 수 있는 식 결과의 최댓값.
둘째 줄에 최솟값 출력.

항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과만 나오도록 입력이 주어진다.
'''

max_val = int(-1e9)
min_val = int(1e9)

n = int(input())
s = list(map(int, input().split()))
o_n = list(map(int, input().split()))

o = []

def dfs():

    global max_val
    global min_val

    if len(o) == n - 1:

        res = s[0]

        for i in range(len(o)):
            
            # 덧셈
            if o[i] == 0:
                res += s[i+1]

            # 뺄셈
            elif o[i] == 1:
                res -= s[i+1]

            # 곱셈
            elif o[i] == 2:
                res *= s[i+1]
            
            # 나눗셈
            else:
                if res < 0:
                    res = -res
                    res //= s[i+1]
                    res = -res

                else:
                    res //= s[i+1]

        if res > max_val:
            max_val = res
        
        if res < min_val:
            min_val = res

        return

    for i in range(len(o_n)):
        for _ in range(o_n[i]):
            o.append(i)
            o_n[i] -= 1
            dfs()
            o.pop()
            o_n[i] += 1

dfs()

print(max_val)
print(min_val)