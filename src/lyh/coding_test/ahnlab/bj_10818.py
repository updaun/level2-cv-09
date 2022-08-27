import sys

def solution(arr):
    max_val, min_val = -1000000, 1000000
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    print(min_val, max_val)

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

solution(arr)