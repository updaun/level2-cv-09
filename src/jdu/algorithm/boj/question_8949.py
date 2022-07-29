import sys
a, b = map(str, sys.stdin.readline().split())
result = ''
if len(a) > len(b):
    big_num = a
    small_num = b
else:
    big_num = b
    small_num = a
for i in range(max(len(a), len(b))):
    diff = abs(len(a) - len(b))
    if i < diff:
        result += big_num[i]
    else:
        result += str(int(small_num[i-diff]) + int(big_num[i]))
print(result)