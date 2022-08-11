# source: https://leetcode.com/problems/combination-sum/
# ref: https://www.youtube.com/watch?v=GBKI9VSKdGg&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=8

'''
candidates: distinct int array
target

return a list of all unique combi of candidates where chosen nums sum to target.
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            
            cur.pop()
            dfs(i+1, cur, total)
            
            
        dfs(0, [], 0)
        
        return res