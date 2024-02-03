# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0

        for operation in operations:
            operand = operation[1] if operation[0] == 'X' else operation[0]
            if operand == '+':
                value += 1
            else:
                value -= 1

        return value
