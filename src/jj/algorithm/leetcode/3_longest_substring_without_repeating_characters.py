# source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''
len of the longest substring without repeating characters
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = len(set(s))
        
        for i in range(max_len, 1, -1):
            for j in range(len(s)-i+1):
                if len(s[j:j+i]) == len(set(s[j:j+i])):
                    return i
        
        if not s:
            return 0
        
        return 1