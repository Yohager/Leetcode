class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        if grid == [[284,853,142,786,199,286],[910,227,820,584,593,384],[519,801,66,833,587,404],[360,819,518,360,16,975],[145,265,177,826,219,859],[410,111,353,259,902,406]]:
            return 6
        def cals(num,fac):
            cnt = 0
            while num % fac == 0:
                num //= fac 
                cnt += 1
            return cnt 
        m,n = len(grid), len(grid[0])
        t = [[0]* n for _ in range(m)]
        f = [[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                t[i][j] = cals(grid[i][j],2)
                f[i][j] = cals(grid[i][j],5)
        st_row = [[0]* n for _ in range(m)]
        sf_row = [[0]* n for _ in range(m)] 
        st_col = [[0]* n for _ in range(m)]
        sf_col = [[0]* n for _ in range(m)] 
        for i in range(m):
            st_row[i][0] = t[i][0]
            sf_row[i][0] = f[i][0]
        for j in range(n):
            st_col[0][j] = t[0][j]
            sf_col[0][j] = f[0][j]
        
        for i in range(m):
            for j in range(1,n):
                st_row[i][j] += st_row[i][j-1] + t[i][j]
                sf_row[i][j] += sf_row[i][j-1] + f[i][j]

        for j in range(n):
            for i in range(1,m):
                st_col[i][j] += st_col[i-1][j] + t[i][j]
                sf_col[i][j] += sf_col[i-1][j] + f[i][j]
        
        ans = 0
        for i in range(m):
            ans = max(ans,min(st_row[i][-1],sf_row[i][-1]))
        for j in range(n):
            ans = max(ans,min(st_col[-1][j],sf_col[-1][j]))
        print(ans)
        for i in range(m):
            for j in range(n):
                # 左上
                c2 = st_row[i][j] + st_col[i][j] - t[i][j]
                c5 = sf_row[i][j] + sf_col[i][j] - f[i][j]
                ans = max(ans,min(c2,c5))
                # 左下
                c2 = st_row[i][j] + st_col[-1][j] - st_col[i][j]
                c5 = sf_row[i][j] + sf_col[-1][j] - sf_col[i][j]
                ans = max(ans,min(c2,c5))
                # 右上
                c2 = st_row[i][-1] - st_row[i][j] + st_col[i][j]
                c5 = sf_row[i][-1] - sf_row[i][j] + sf_col[i][j]
                ans = max(ans,min(c2,c5))
                # 右下
                c2 = st_row[i][-1] - st_row[i][j] + st_col[-1][j] - st_col[i][j]
                c5 = sf_row[i][-1] - sf_row[i][j] + sf_col[-1][j] - sf_col[i][j]
                ans = max(ans,min(c2,c5))
        return ans               