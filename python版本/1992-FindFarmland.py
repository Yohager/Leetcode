class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        if not land:
            return []
        ans = []
        m,n = len(land), len(land[0])
        arr = [[0]*(n+2) for _ in range(m+2)]
        for i in range(m):
            for j in range(n):
                arr[i+1][j+1] = land[i][j]
        #print(arr)
        for x in range(1,m+1):
            for y in range(1,n+1):
                if arr[x][y] == 1 and arr[x-1][y] == 0 and arr[x][y-1] == 0:
                    td,tw = x,y 
                    while arr[td][y] == 1:
                        td += 1
                    while arr[x][tw] == 1:
                        tw += 1
                    ans.append([x-1,y-1,td-2,tw-2])
        return ans 