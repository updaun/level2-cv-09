import sys

def solution(arr):
    max_val, people = 0, 0

    for leave, getin in arr:
        people -= leave
        people += getin
        if people > max_val:
            max_val = people
    
    print(max_val)


arr = list()
for _ in range(10):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

solution(arr)