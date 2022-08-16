order = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, input().split())
result = ''
while n >= b:
    n, temp = divmod(n, b)
    result += order[temp]
result += order[n]
print(result[::-1])