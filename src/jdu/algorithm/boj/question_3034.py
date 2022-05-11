import sys
N, W, H = list(map(int, sys.stdin.readline().split()))
n_list = []
for i in range(N):
    k = int(sys.stdin.readline())
    n_list.append(k)
    
for k in n_list:
    threshold = (W**2+H**2)**0.5
    if k <= threshold:
        print("DA")
    else:
        print("NE")