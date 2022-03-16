class Solution:
    def digArtifacts(self, n: int, arts: List[List[int]], dig: List[List[int]]) -> int:
        def check(r1,c1,r2,c2):
            for r in range(r1,r2+1):
                for c in range(c1,c2+1):
                    if not vis[r][c]:
                        return False 
            return True 
        vis = [[0]*n for _ in range(n)]
        for x,y in dig:
            vis[x][y] = 1
        
        ans = 0
        
        for x1,y1,x2,y2 in arts:
            if check(x1,y1,x2,y2):
                ans += 1
        return ans 