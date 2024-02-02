# https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for num in range(1, n + 1):
            value = ''
            if num % 3 == 0 or num % 5 == 0:
                if num % 3 == 0:
                   value += 'Fizz'
                if num % 5 == 0:
                    value += 'Buzz'
            else:
                value = str(num)
            result.append(value)
        return result
