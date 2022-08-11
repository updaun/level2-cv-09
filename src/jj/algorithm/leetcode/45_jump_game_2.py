# source: https://leetcode.com/problems/jump-game-ii/

'''
nums: array of non-negative ints

initially positioned at the first index of the array
element in the array represents max jump len at that pos.

goal is to reach the last index in the min num of jumps.

always able to reach the last index.
'''

'''
1 <= nums.len <= 10^4
0 <= nums[i] <= 1000
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        pos = 0
        ans = 0
        
        while pos < len(nums) - 1:
            
            max_jump = 0
            index = 0
            
            for i in range(nums[pos]):
                
                if pos + i + 1 == len(nums) - 1:
                    return ans + 1
                
                if max_jump < i+1 + nums[pos+i+1]:
                    max_jump = i+1 + nums[pos+i+1]
                    index = pos + i + 1
                
            ans += 1
            pos = index
            
        return ans
                