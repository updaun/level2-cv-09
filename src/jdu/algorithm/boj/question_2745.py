order = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()
n = n[::-1]
result = 0
for i in range(len(n)):
    result += int(b)**i*order.index(n[i])
print(result)