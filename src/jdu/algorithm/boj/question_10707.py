import sys
input = sys.stdin.readline
input_value = []
for i in range(5):
    input_value.append(int(input()))
A, B, C, D, P = input_value
if C < P:
    print(min(A*P, B+(P-C)*D))
else:
    print(min(A*P, B))