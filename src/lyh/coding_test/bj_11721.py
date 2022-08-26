import sys
str_input = sys.stdin.readline().rstrip()

N = len(str_input) // 10

for i in range(N):
    print(str_input[i*10:i*10+10])
print(str_input[N*10:])