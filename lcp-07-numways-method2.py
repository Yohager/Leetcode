class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        #构建一个邻接矩阵
        # adjmatrix = [[0 for _ in range(n)] for _ in range(n)]
        # for elem in relation:
        #     adjmatrix[elem[0]][elem[1]] = 1
        d = collections.defaultdict(set)
        for x,y in relation:
            d[x].add(y)
        def dfs(i,steps):
            if steps == k:
                if i == n-1:
                    self.cnt += 1
                return  
            if steps > k:
                return 
            for x in d[i]:
                dfs(x,steps+1)
        self.cnt = 0
        dfs(0,0)
        return self.cnt