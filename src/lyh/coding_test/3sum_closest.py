# implementation task by leetcode
# Solve by two - pointer approach

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        
        N = len(nums)
        ans = float('inf')
        
        for i in range(N):
            j = i+1
            k = N-1
            
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                if total==target: return total
                if abs(target-ans)>abs(target-total): ans = total
				
                if total>target:
                    k -= 1
                elif total<target:
                    j += 1
        return ans