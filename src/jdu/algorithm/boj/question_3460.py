n = int(input())
for i in range(n):
    result = ''
    target = str(bin(int(input())))[2:]
    target = target[::-1]
    for s in range(len(target)):
        if target[s] == "1":
            result += str(s)
            result += " "
    print(result.rstrip())

