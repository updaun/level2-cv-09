import sys
input = sys.stdin.readline
for i in range(int(input())):
    result = 0
    input_bit = input().rstrip()[::-1]
    for b in range(len(input_bit)):
        result += int(input_bit[b])*(2**(b))
    print(result)
