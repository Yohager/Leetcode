class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0:
            return False
        n = len(matrix)
        m= len(matrix[0])
        l = 0
        r = m-1
        while (l < n and r >= 0):
            if (target == matrix[l][r]):
                return True
            elif (target < matrix[l][r]):
                r -= 1
            else:
                l += 1
        return False