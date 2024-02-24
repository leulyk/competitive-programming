# https://leetcode.com/problems/diagonal-traverse/description/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up = True 
        diagonal = []

        i = 0
        j = 0
        row_length = len(mat)
        col_length = len(mat[0])

        if row_length == 1:
            return mat[0]

        while i < row_length and j < col_length:
            diagonal.append(mat[i][j])  
            if up:
                while i - 1 >= 0 and j + 1 < col_length:
                    diagonal.append(mat[i - 1][j + 1])
                    i -= 1
                    j += 1
                up = False
                if j == col_length - 1:
                    i += 1 
                else:
                    j += 1
            else:
                while i + 1 < row_length and j - 1 >= 0:
                    diagonal.append(mat[i + 1][j - 1])
                    i += 1
                    j -= 1
                up = True
                if i == row_length - 1:
                    j += 1
                else:
                    i += 1

        return diagonal
