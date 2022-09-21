# LeetCode Easy

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp_num, mul = 0, 1
        for digit in digits[::-1]:
            temp_num += digit * mul
            mul *= 10
        temp_num += 1
        
        answer = list()
        while temp_num:
            answer.append(temp_num % 10)
            temp_num //= 10
        
        return answer[::-1]