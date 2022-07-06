start, end = map(int, input().split())
target = [0]
temp = 0
for i in range(1, 46):
    for j in range(i):
        temp += i
        target.append(temp)
print(target[end]-target[start-1])