# LeetCode Easy

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        answer = ""
        max_len = max(len(a), len(b))
        min_len = min(len(a), len(b))
        if len(a) == min_len:
            a = "0" * (max_len - min_len) + a
        if len(b) == min_len:
            b = "0" * (max_len - min_len) + b
        
        carry = 0
        for a_c, b_c in zip(a[::-1], b[::-1]):
            temp_sum = carry + int(a_c) + int(b_c)
            carry = 0
            if temp_sum < 2:
                answer += str(temp_sum)
            else:
                answer += str(temp_sum - 2)
                carry = 1
        if carry:
            answer += str(carry)
        
        return answer[::-1]