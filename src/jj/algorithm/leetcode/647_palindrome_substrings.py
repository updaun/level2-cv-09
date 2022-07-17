# source: https://leetcode.com/problems/palindromic-substrings/
# ref: https://www.youtube.com/watch?v=4RACzI5-du8

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # odd length palindrome
            l = r = i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
            # even length palindrome
            l = i
            r = i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
        return res