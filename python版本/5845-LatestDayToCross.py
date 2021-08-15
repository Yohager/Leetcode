class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        '''
        第一种方法：二分查找+广度优先搜索
        '''
        from collections import deque 
        l,r = 0, row * col
        ans  = 0 
        while l <= r:
            m = (l+r) // 2
            grid = [[1] * col for _ in range(row)]
            for x,y in cells[:m]:
                grid[x-1][y-1] = 0
            q = deque()
            for k in range(col):
                if grid[0][k] == 1:
                    q.append((0,k))
                    grid[0][k] = 0
            find = False
            while q:
                c_x, c_y = q.popleft()
                for nx,ny in [(c_x-1,c_y),(c_x+1,c_y),(c_x,c_y-1),(c_x,c_y+1)]:
                    #四个方向
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny]:
                        if nx == row - 1:
                            #如果当前是最后一排那么就联通了
                            find = True 
                            break 
                        q.append((nx,ny))
                        grid[nx][ny] = 0
            if find:
                ans = m 
                l = m + 1
            else:
                r = m - 1
        return ans 
