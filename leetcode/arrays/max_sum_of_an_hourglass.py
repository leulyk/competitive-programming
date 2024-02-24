# https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_sum = 0 

        for i in range(1, row - 1):
            for j in range(1, col - 1):
                sum = 0 
                sum += grid[i][j] + grid[i - 1][j] + grid[i + 1][j]
                sum += grid[i - 1][j - 1] + grid[i - 1][j + 1]
                sum += grid[i + 1][j - 1] + grid[i + 1][j + 1]
                if sum > max_sum:
                    max_sum = sum
        
        return max_sum

