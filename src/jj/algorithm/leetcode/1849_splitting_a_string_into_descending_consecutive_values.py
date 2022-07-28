# source: https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
# ref: https://www.youtube.com/watch?v=eDtMmysldaw&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=7

'''
check if 's' can be split into two or more non-empty substrings such that the numerical values of the substrings are in desc ord & the diff bet num values of every two adj substrings is equal to 1.
'''

class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(index, prev):
            if index == len(s):
                return True
            
            for j in range(index, len(s)):
                val = int(s[index:j+1])
                
                if val + 1 == prev and dfs(j+1, val):
                    return True
            
            return False
    
        for i in range(len(s) - 1):
            val = int(s[:i+1])
        
            if dfs(i+1, val): return True
    
        return False
        