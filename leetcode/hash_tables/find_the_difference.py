# https://leetcode.com/problems/find-the-difference/description/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_dict = {}

        for char in s:
            if char_dict.get(char):
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        
        for char in t:
            if not char_dict.get(char):
                return char
            else:
                char_dict[char] -= 1
                if char_dict[char] == 0:
                    del char_dict[char]
