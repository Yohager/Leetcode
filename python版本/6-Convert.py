class Solution:
    def convert(self, s: str, r: int) -> str:
        if r == 1:
            return s 
        n = len(s)
        times = n // (2*r -2)
        left = n % (2*r - 2)
        cols = times * (r-1)
        if left <= r:
            cols += 1
        else:
            cols += (left - r + 1)
        
        matrix = [['']* cols for _ in range(r)]
        for i in range(times):
            cur = s[i*(2*r-2):(i+1)*(2*r-2)] # 一次从s中取出(2r-2)个字符
            # print(cur)
            '''
            共计2r-2个元素，当前第一列填充r个元素
            后续的r-2列填充r-2个元素
            '''
            for j in range(r):
                matrix[j][i*(r-1)] = cur[j]
            idx = 1
            for k in range(i*(r-1)+1,(i+1)*(r-1)):
                # print(cur[r-idx+1])
                matrix[r-idx-1][k] = cur[r-1+idx]
                idx += 1     
        # 处理剩余的一些字符
        # print(matrix)
        l = s[times*(2*r-2):]
        # print(l)
        if left <= r:
            for i in range(left):
                matrix[i][cols-1] = l[i]
        else:
            for j in range(r):
                matrix[j][times*(r-1)] = l[j]
            num = left - r # 表示当前填充完最后一轮的第一列后还剩余多少个元素未填入
            # print(num)
            # 行数从 r-2开始到r-2+num
            # 列数从times*(r-1)+1开始到times*(r-1)+1+num
            # print(matrix)
            final = s[times*(2*r-2)+r:]
            # print(final,num)
            # print(matrix[7])
            for k in range(num):
                matrix[r-2-k][times*(r-1)+1+k] = final[k]
        
        # 遍历一遍matrix
        #print(matrix)
        ans = ''
        for x in matrix:
            ans += (''.join(x))
        return ans 