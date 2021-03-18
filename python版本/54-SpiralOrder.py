class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        ans = []
        l = len(matrix)
        w = len(matrix[0])
        cnt = 0
        x,y = 0,0
        left,right,up,down = 0,w-1,0,l-1
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        cur = 0
        #退出的依据是所有的元素都被访问过了
        while cnt != l * w:
            ans.append(matrix[x][y])
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