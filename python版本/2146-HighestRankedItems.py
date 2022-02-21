class Solution:
    def highestRankedKItems(self, grid: List[List[int]], p: List[int], s: List[int], k: int) -> List[List[int]]:
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        cads = {}
        m,n = len(grid), len(grid[0])
        # for i in range(m):
        #     for j in range(n):
        #         if p[0] <= grid[i][j] <= p[1]:
        #             cads[(i,j)] = [float('inf'),grid[i][j]]
        #print(cads)
        # 更新从start到cads中的所有元素的dist
        q = deque([(s[0],s[1])])
        steps = 0
        vis = [[False]*n for _ in range(m)]
        while q:
            cur_len = len(q)
            for _ in range(cur_len):
                x,y = q.popleft() #当前弹出的pos
                vis[x][y] = True
                if p[0] <= grid[x][y] <= p[1]:
                    cads[(x,y)] = steps
                for dx,dy in dirs:
                    if 0 <= x+dx < m and 0 <= y+dy < n:
                        if grid[x+dx][y+dy] == 0:
                            continue 
                        else:
                            if vis[x+dx][y+dy]:
                                continue 
                            else:
                                q.append((x+dx,y+dy))
                                vis[x+dx][y+dy] = True
            steps += 1
        # print(cads)
        p = []
        for key in cads:
            p.append([cads[key],grid[key[0]][key[1]],key[0],key[1]])
        p.sort()
        ans = []
        if len(p) < k:
            for i in range(len(p)):
                ans.append([p[i][-2],p[i][-1]])

        else:
            for i in range(k):
                ans.append([p[i][-2],p[i][-1]])
        return ans 
                
            