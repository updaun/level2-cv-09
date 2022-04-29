# implementation task by leetcode
# Solve by brute-force

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefix = ""
        
        
        for i, token in enumerate(strs[0]):
            count = 1
            for word in strs[1:]:
                if len(word) > i and word[i] == token:
                    count += 1
                if len(word) <= i or word[i] != token:
                    return longest_prefix
            if count == len(strs):
                longest_prefix += token
        
        return longest_prefix