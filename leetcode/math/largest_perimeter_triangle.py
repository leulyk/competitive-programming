# https://leetcode.com/problems/largest-perimeter-triangle/description/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        for index in range(len(nums) - 1, 1, -1):
            if nums[index - 1] + nums[index - 2] > nums[index]:
                return nums[index - 1] + nums[index - 2] + nums[index]
        
        return 0
