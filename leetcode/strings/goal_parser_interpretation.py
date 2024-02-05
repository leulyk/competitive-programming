# https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        index = 0 
        parsed_text = ''
        while index < len(command):
            if command[index] == 'G':
                parsed_text += 'G'
                index += 1
            elif command[index + 1] == ')':
                parsed_text += 'o'
                index += 2
            else:
                parsed_text += 'al'
                index += 4
        
        return parsed_text
