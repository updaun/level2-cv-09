b = input()
d = int(b, 2)
print(oct(d)[2:])

# 시간초과
# b = input()
# d = 0
# for i in range(len(b)):
#     d += int(b[::-1][i]) * (2**i)
# print(oct(d)[2:])