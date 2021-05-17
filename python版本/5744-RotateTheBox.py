class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box)
        m = len(box[0])
        for i in range(n):
            #使用一个队列来存放空位，如果遇到一个空位就将其放入队列中；如果遇到一个石头就消费队列中的一个空位；如果遇到障碍就将队列清空表示那些都不行
            #队列为空则表示没有空位了，那么石头就不动
            q = deque()
            for j in range(m-1,-1,-1):
                if box[i][j] == '*':
                    q.clear()
                elif box[i][j] == '#':
                    if q:
                        pos = q.popleft()
                        box[i][pos] = '#'
                        box[i][j] = '.'
                        q.append(j)
                else:
                    q.append(j)
        ans = [[""] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][n - i - 1] = box[i][j]
        return ans 