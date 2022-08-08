import sys
input = sys.stdin.readline
g = [1,2,3,3,4,10]
s = [1,2,2,2,3,5,10]
n = int(input())
for i in range(n):
    g_p = [val*g[id] for id, val in enumerate(list(map(int, input().split())))]
    s_p = [val*s[id] for id, val in enumerate(list(map(int, input().split())))]
    if sum(g_p) == sum(s_p):
        print(f"Battle {i+1}: No victor on this battle field")
    elif sum(g_p) > sum(s_p):
        print(f"Battle {i+1}: Good triumphs over Evil")
    else:
        print(f"Battle {i+1}: Evil eradicates all trace of Good")
