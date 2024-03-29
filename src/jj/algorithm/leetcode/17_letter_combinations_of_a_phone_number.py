# source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# ref: https://www.youtube.com/watch?v=0snEunUacZY&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=6

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        res = []
        
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i+1, curStr+c)
        
        if digits: backtrack(0, '')
            
        return res
        
        