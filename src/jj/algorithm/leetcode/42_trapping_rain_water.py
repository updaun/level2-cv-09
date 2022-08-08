# source: https://leetcode.com/problems/trapping-rain-water/submissions/
# ref: https://www.youtube.com/watch?v=ZI2z5pq0TqA&list=PLot-Xpze53letfIu9dMzIIO7na_sqvl0w&index=3

'''
n: height.length
1 <= n <= 2 * 10^4
'''

'''
take min of maxL & maxR
=> min(L, R) - height[i]
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                
        return res
        