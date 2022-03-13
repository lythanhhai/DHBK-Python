from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        count = 0
        arr = []
        res = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(0, row):
            if i == row - 1:
                break
            else:
                for j in range(0, col):
                    if j == col - 1:
                        break
                    else:
                        for k in range(i,  row):
                            for l in range(j, col):
                                if k - i == l - j and matrix[i][j] == matrix[k][l] and k - i != 0 and l - j != 0:
                                    count += 1
                        arr.append(count)
                        count = 0
        for i in arr:
            if i != 0:
                res.append(i)
        if len(res) == row * col - (row + col - 1):
            return True
        else:
            return False
            
a = Solution()
#print(a.isToeplitzMatrix([[1,2],[2, 2]]))
print(a.isToeplitzMatrix([[53,64,90,98,34],
                          [91,53,64,90,98],
                          [17,91,53,64,0]]))