class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        dirs = [(0,1),(1,0)]
        m,n = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(i,j,v):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == '(':
                v += 1
            if grid[i][j] == ')':
                v -= 1
            if v < 0:
                return False 
            if i == m-1 and j == n-1:
                # 到达check一下是否满足条件
                if v == 0:
                    return True 
                else:
                    return False 
            for d in dirs:
                if dfs(i+d[0],j+d[1],v):
                    return True 
            return False 
        return dfs(0,0,0)
                
            
            