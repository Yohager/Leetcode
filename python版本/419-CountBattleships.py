class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m,n = len(board), len(board[0])
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == '.':
                return False 
            board[i][j] = '.'
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(i+dx,j+dy)
            return True
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if dfs(i,j):
                    ans += 1
        return ans 