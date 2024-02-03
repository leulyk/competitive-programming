# https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ''

        index = 0
        
        while index < len(word1) or index < len(word2):
            if index < len(word1):
                merged_word += word1[index]
            if index < len(word2):
                merged_word += word2[index]
            index += 1

        return merged_word
