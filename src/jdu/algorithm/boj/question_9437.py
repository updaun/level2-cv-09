import sys
input = sys.stdin.readline
while True:
    input_str = input().rstrip()
    if input_str == "0":
        break
    n, p = map(int, input_str.split())
    papers = []
    for i in range(int(n/4)):
        papers.append([2*i+1, 2*i+2, n-(2*i+1), n-2*i])
    for i in papers:
        if p in i:
            i.remove(p)
            print(" ".join(map(str, i)))