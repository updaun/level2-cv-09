# LeetCode Easy

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.strip().split()
        return len(word_list[-1])