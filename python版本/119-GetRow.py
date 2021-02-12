class Solution:
    def getRow(self, r: int) -> List[int]:
        if r == 0:
            return [1]
        if r == 1:
            return [1,1]
        ans = [[1],[1,1]]
        for i in range(1,r):
            tmp = [1]
            for k in range(len(ans[i])-1):
                tmp.append(ans[i][k]+ans[i][k+1])
            tmp.append(1)
            ans.append(tmp)
       #print(ans)
        return ans[-1]