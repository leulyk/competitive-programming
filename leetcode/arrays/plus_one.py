# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = [0] * len(digits)
        carry = 0
        
        for index in range(len(digits) - 1, -1, -1):
            sum = digits[index] + 1 if index == len(digits) - 1 else digits[index] + carry
            result[index] = sum % 10
            carry = sum // 10
        
        if carry:
            return [carry] + result
        return result
