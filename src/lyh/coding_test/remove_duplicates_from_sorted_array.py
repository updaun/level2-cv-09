# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# implementation task by leetcode
# Solve by brute-force

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos, pos_num = 1, nums[0]
        for i, num in enumerate(nums):
            if i > 0 and num > pos_num:
                nums[pos] = num
                pos_num = num
                pos += 1
        return pos
        