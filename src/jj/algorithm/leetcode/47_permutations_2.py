# https://leetcode.com/problems/permutations-ii/

from itertools import groupby

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = list(map(list, permutations(nums, len(nums))))
        
        res = []
        
        for p in perm:
            if p not in res:
                res.append(p)
        
        return res