class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        import math
        n = len(points)
        dist_mat = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                dist_mat[i][j] = (abs(points[i][0]-points[j][0]))**2 + (abs(points[i][1]-points[j][1]))**2
                dist_mat[j][i] = (abs(points[i][0]-points[j][0]))**2 + (abs(points[i][1]-points[j][1]))**2
        ans = 0
        for x in dist_mat:
            tmp = collections.Counter(x)
            for k in tmp:
                if tmp[k] >= 2:
                    ans += (tmp[k]*(tmp[k]-1))
        return ans 