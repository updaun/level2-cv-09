# source: https://www.acmicpc.net/problem/22864

'''
하루에 한 시간 단위로 일 or 쉬기.
하루에 한 시간 일하면 피로도 A, 일 B만큼 처리.
한 시간 쉬면 피로도 C만큼 줄어든다.
피로도 음수로 내려가면 0.

피로도를 최대한 M을 넘지 않게. 

M을 넘지 않도록 하루에 최대 얼마나 일을 할 수 있는지.
하루 24시간.
'''

'''
입력
첫 번째 줄: A, B, C, M
initial 피리도: 0
'''

'''
A: 일로 인한 피로도
B: 처리할 수 있는 양
C: 피로도 감소
M: 넘기면 번아웃
'''

'''
출력 하루에 번아웃이 오지 않도록 최대 얼마나 일을 할 수 있는지.
'''

a, b, c, m = list(map(int, input().split()))

tired = 0
output = 0
time = 0

while time < 24:
    time += 1

    # 일로 인한 피로도가 m을 넘지 않으면 일하기
    if tired + a <= m:
        tired += a
        output += b
    
    # 넘으면 쉬기
    else:
        tired -= c

        if tired < 0:
            tired = 0

print(output)