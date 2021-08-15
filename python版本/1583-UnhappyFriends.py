class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        orders = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n-1):
                orders[i][preferences[i][j]] = j 
        ans = 0
        match = [0] * n
        for x,y in pairs:
            match[x] = y
            match[y] = x 
        for k in range(n):
            tmp = match[k]
            #当前k匹配的人是tmp
            #下面检查tmp前面的更偏好的人有没有不开心的
            idx = orders[k][tmp]
            for elem in range(idx):
                u = preferences[k][elem]
                v = match[u]
                if orders[u][k] < orders[u][v]:
                    ans += 1
                    break 
        return ans 