# source: https://leetcode.com/problems/subsets/

from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        for i in range(len(nums)+1):
            combination = list(map(list, combinations(nums, i)))
            
            for c in combination:
                ans.append(c)
            
        return ans