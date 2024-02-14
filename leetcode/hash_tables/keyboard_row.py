# https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {}
        for num in range(ord('a'), ord('z') + 1):
            if chr(num) in 'qwertyuiop':
                rows[chr(num)] = 1
            elif chr(num) in 'asdfghjkl':
                rows[chr(num)] = 2
            elif chr(num) in 'zxcvbnm':
                rows[chr(num)] = 3

        result = []
        for word in words:
            row = 0
            for index, char in enumerate(word):
                if index == 0:
                    row = rows[char.lower()]
                else:
                    if rows[char.lower()] != row:
                        break
            else:
                result.append(word)
        
        return result
