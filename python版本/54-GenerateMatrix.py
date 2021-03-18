class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        ans = [[0 for _ in range(n)] for _ in range(n)]
        x,y = 0,0
        left,right,up,down = 0,n-1,0,n-1
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        cur = 0
        cnt = 1
        #退出的依据是所有的元素都被访问过了
        while cnt <= n**2:
            ans[x][y] = cnt 
            cnt += 1
            if cur == 0 and y == right:
                cur += 1
                #修改边界
                up += 1
            elif cur == 1 and x == down:
                cur += 1
                right -= 1
            elif cur == 2 and y == left:
                cur += 1
                down -= 1
            elif cur == 3 and x == up:
                cur += 1
                left += 1


            cur %= 4
            x += directions[cur][0]
            y += directions[cur][1]
        return ans