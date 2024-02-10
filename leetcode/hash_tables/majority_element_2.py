# https://leetcode.com/problems/majority-element-ii/description/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequencies = {} 
        majority_elements = set()

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

            if frequencies[num] > len(nums) // 3:
                majority_elements.add(num)
        
        return list(majority_elements)
