import sys

def solution(inputs):
    for num in inputs:
        temp, idx = list(), 0
        while num:
            if num % 2:
                temp.append(idx)
            num //= 2
            idx += 1
        print(' '.join(map(str, temp)))

inputs = list()
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    inputs.append(int(sys.stdin.readline().rstrip()))

solution(inputs)