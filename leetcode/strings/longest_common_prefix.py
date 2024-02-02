# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = None
        for str in strs:
            length = len(str)
            if min_length == None or length < min_length:
                min_length = length
        
        index = 0
        while index < min_length:
            for i in range(len(strs) - 1):
                if strs[i][index] != strs[i + 1][index]:
                    break
            else:
                index += 1
                continue
            break
        
        return strs[0][:index]
