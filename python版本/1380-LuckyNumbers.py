class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        ans = []
        minv_row = []
        for r in matrix:
            minv_row.append(min(r))
        
        maxv_col = []
        for c in zip(*matrix):
            maxv_col.append(max(c))
        return [x for x in minv_row if x in maxv_col]