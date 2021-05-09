class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ans = []
        l = 1950
        r = 2050
        for i in range(l,r):
            cnt = 0
            for j in logs:
                if i >= j[0] and i <= j[1]-1:
                    cnt += 1
            ans.append([cnt,i])
        ans.sort(reverse=True,key=lambda x: (x[0],-x[1]))
        #print(ans)
        return ans[0][1]
        