# https://leetcode.com/problems/delete-columns-to-make-sorted/description/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        unsorted_count = 0 

        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j][i] > strs[j + 1][i]:
                    unsorted_count += 1
                    break
        
        return unsorted_count

