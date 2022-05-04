# implementation task by leetcode
# Solve by array in-place with O(1) extra memory

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[idx] = num
                idx += 1
        return idx