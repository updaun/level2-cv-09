import sys
result = 0
for i in range(8):
    c = sys.stdin.readline()
    if i % 2 == 0:
        for j in range(4):
            if c[2*j] == "F":
                result += 1
    else:
        for j in range(4):
            if c[2*j+1] == "F":
                result += 1
print(result)