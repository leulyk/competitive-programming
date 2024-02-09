# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        return sum(range(0, len(nums) + 1)) - sum(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        nums.sort()

        for index in range(len(nums)):
            if nums[index] != index:
                return index

        return len(nums)
