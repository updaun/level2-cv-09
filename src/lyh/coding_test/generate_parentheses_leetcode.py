# DynamicProgramming task
# Solve it by finding all possible cases and then verifying them

from itertools import *

class Solution(object):
    def __init__(self):
        self.output = []
        self.left = "("
        self.right = ")"
        self.valid = 81

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for word in s:
            if word in self.left:
                self.output.append(ord(word))
            if word in self.right:
                if not self.output:
                    return False
                if self.output.pop() + ord(word) != self.valid:
                    return False
        return not bool(self.output)
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = list()
        initial_sentence = [")" for _ in range(n*2)]
        initial_sentence[0] = "("
        left_idx_list = [x for x in range(1,n*2-1)]
        for x in combinations(left_idx_list, n-1):
            temp = initial_sentence[:]
            for i in x:
                temp[i] = "("
            sentence = "".join(temp)
            if self.isValid(sentence):
                answer.append("".join(temp))
        
        return answer