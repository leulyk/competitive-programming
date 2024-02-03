# https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ''

        for char in address:
            if char == '.':
               defanged += '[.]'
            else:
                defanged += char

        return defanged
