# source: https://leetcode.com/problems/two-sum/

'''
nums: array
target: int

return two indices of the 2 nums to add up to target (only 1 ans exists)

less than O(n^2)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        