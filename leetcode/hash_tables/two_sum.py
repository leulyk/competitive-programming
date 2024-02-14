# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_hash = {}

        for index in range(len(nums)):
            index_hash[nums[index]] = index
        
        for index in range(len(nums)):
            value = target - nums[index]
            if value in index_hash and index_hash[value] != index:
                return [index, index_hash[value]]
