class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if matrix == []:
            return True
        if n == 1 or m == 1:
            return True
        for i in range(m-1):
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False
        return True