class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        c = set(list(range(1,n+1)))
        for m in matrix:
            if set(m) != c:
                return False 
        for i in range(n):
            cur = set([matrix[x][i] for x in range(n)])
            if cur != c:
                return False 
        return True 