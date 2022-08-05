n = int(input())
result = []
target = [i for i in range(1, n+1)]
for i in range(n):
    if len(target) > 1:
        result.append(target.pop(0))
        target = target[1:]+[target[0]]
    else:
        result.append(target[0])
print(" ".join(map(str, result)))