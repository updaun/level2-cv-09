import sys
import math
temp = 1
num_type = ["odd", "even"]
while True:
    n0 = int(sys.stdin.readline())
    if n0 == 0:
        break 
    n1 = 3*n0
    n2 = math.ceil(n1/2)
    n3 = 3*n2
    n4 = n3//9
    print(f"{temp}. {num_type[int(n1 % 2 == 0)]} {n4}")
    temp += 1