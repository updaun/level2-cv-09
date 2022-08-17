# DP(72ms)
n = int(input())
d = [5001]*(n+5)
d[3] = d[5] = 1
for i in range(6, n+1):
    d[i] = min(d[i-3], d[i-5]) + 1
print(d[n] if d[n] < 5001 else -1)

# 그리디 알고리즘(96ms)
sugar = int(input())
bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1
else:
    print(-1)


# 그리디 알고리즘(68ms)
n = int(input())
cnt = 0
while n >= 5:
    n -= 5
    cnt += 1
if n == 1:
    if cnt == 0:
        print(-1)
    else:
        cnt += 1
        print(cnt)
elif n == 2:
    if cnt > 1:
        cnt += 2
        print(cnt)
    else:
        print(-1)
elif n == 3:
    cnt += 1
    print(cnt)
elif n == 4:
    if cnt == 0:
        print(-1)
    else:
        cnt += 2
        print(cnt)
else:
    print(cnt)