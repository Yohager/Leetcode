class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
        records = dict()
        def dfs(t,i,j):
            # t: times, (i,j): position
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0 
            if t == 0:
                return 1 
            if (t,i,j) in records:
                return records[(t,i,j)]
            tmp = 0
            for dx,dy in dirs:
                tmp += dfs(t-1,i+dx,j+dy)
            # tmp /= 8.0
            records[(t,i,j)] = tmp 
            return tmp 
        return dfs(k,row,column) / (8.0)**k