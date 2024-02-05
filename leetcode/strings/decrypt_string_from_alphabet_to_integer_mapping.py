# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypted_string = '' 
        index = 0

        while index < len(s):
            if (s[index] == '1' or s[index] == '2') and index + 2 < len(s) and s[index + 2] == '#':
                decrypted_string += chr(ord('a') + int(s[index: index + 2]) - 1)
                index += 3
            else:
                decrypted_string += chr(ord('a') + int(s[index]) - 1)
                index += 1
        
        return decrypted_string
