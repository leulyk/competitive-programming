# https://leetcode.com/problems/apply-operations-to-an-array/description/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums) - 1): 
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0
            
        index = 0 
        zeroes = 0
        while index < len(nums):
            if nums[index] == 0:
                nums.pop(index)
                zeroes += 1 
            else:
                index += 1
        
        nums += ([0] * zeroes)
        
        return nums
