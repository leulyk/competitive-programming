# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/description/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        one_third = num // 3 
        if one_third * 3 == num:
            return [one_third - 1, one_third, one_third + 1]
        return []
