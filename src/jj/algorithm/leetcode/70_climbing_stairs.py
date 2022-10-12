# source: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for _ in range(n+1)]
        
        memo[1] = 1
        if n >= 2: memo[2] = 1
        
        for i in range(1, n+1):
            if i+1 <= n: memo[i+1] += memo[i]
            if i+2 <= n: memo[i+2] += memo[i]
                
        return memo[n]