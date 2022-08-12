import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = [i for i in range(1, n+1)]
def switch_list(n_list, start, finish):
    return n_list[:start]+n_list[start:finish][::-1]+n_list[finish:]
for i in range(m):
    s, f = map(int, input().split())
    n_list = switch_list(n_list, s-1, f)
print(" ".join(map(str, n_list)))