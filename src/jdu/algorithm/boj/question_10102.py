import sys
V = int(sys.stdin.readline())
CA = sys.stdin.readline().count("A")
if CA > V/2:
    print("A")
elif CA == V/2:
    print("Tie")
else:
    print("B")