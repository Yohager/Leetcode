class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        for x,y in enumerate(mat):
            ans.append([x,sum(y)])
        ans.sort(key=lambda x:x[1])
        res = []
        for i in range(k):
            res.append(ans[i][0])
        return res 
