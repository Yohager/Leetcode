class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        dirs = [(0,1),(1,1),(0,0),(0,-1),(-1,-1),(-1,1),(1,0),(-1,0),(1,-1)]
        m,n = len(img), len(img[0])
        ans = [[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cur = 0
                cnt = 0
                for dx,dy in dirs:
                    if 0 <= i+dx < m and 0 <= j+dy < n:
                        cur += img[i+dx][j+dy]
                        cnt += 1
                ans[i][j] = math.floor(cur/cnt)
        return ans 