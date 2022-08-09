n = int(input())
for i in range(n):
    temp = 0
    c = int(input())
    while True:
        if c == 1:
            print(temp)
            break
        temp += 1
        if temp*(temp+1) > c:
            print(temp-1)
            break
    