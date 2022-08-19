# Leetcode


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        for i, x in enumerate(haystack):
            if x == needle[0] and i+len(needle) <= len(haystack):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1