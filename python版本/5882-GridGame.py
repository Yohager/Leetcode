class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        def func(grid1):
            sum1 = [grid1[0][0]]
            sum2 = [grid1[1][0]]
            tmp1 = grid1[0][0]
            tmp2 = grid1[1][0]
            for i in range(1,n):
                tmp1 += grid1[0][i]
                sum1.append(tmp1)
                tmp2 += grid1[1][i]
                sum2.append(tmp2)
            return sum1,sum2
        
        p1sum1,p1sum2 = func(grid)
        left = p1sum1[-1] - p1sum1[0]
        right = p1sum2[n-2]
        idx = 0
        minval = float('inf')
        for i in range(1,n-1):
            tmp = max(p1sum1[-1] - p1sum1[i],p1sum2[i-1])
            minval = min(minval,tmp)
        minval = min(minval,left,right)
        return minval