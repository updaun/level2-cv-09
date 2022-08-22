import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
d = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0
for i in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
d = [sorted(d[i]) for i in range(n+1)]

def dfs(curr):
    visited[curr] = True
    for next in d[curr]:
        if not visited[next]:
            dfs(next)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)