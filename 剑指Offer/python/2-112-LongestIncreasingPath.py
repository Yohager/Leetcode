class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        if m == 0 and n == 0:
            return 0 
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        lengths = [[0]*n for _ in range(m)]
        l = 0
        @lru_cache()
        def dfs(i,j):
            if lengths[i][j] != 0:
                return lengths[i][j]
            l = 1
            for dx,dy in directions:
                if 0 <= i+dx < m and 0 <= j+dy < n:
                    if matrix[i+dx][j+dy] > matrix[i][j]:
                        tmp = dfs(i+dx,j+dy)
                        l = max(l,tmp+1)
            lengths[i][j] = l
            return l
        ans = 0
        for i in range(m):
            for j in range(n):
                p = dfs(i,j)
                #lengths[i][j] = p
                ans = max(ans,p)
        #print(lengths)
        return ans 
                
                
            
            
            