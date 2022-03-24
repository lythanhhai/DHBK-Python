import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        T = r * c
        if row * col != T:
            return mat
        output = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(row):
            for j in range(col):
                output[k // c][k % c] = mat[i][j]
                k += 1
        return output