# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        temp = x
        
        while temp != 0:
            current = temp % 10
            reverse = reverse * 10 + current
            temp = temp // 10

        if x == reverse:
            return True
        return False
