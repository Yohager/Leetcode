class Solution:
    def numberOfWays(self, s: str) -> int:
        '''
        合法的操作101或者010
        使用前缀和，维护每个位置左右两边1和0的数量
        '''
        n = len(s)
        pre0 = [0]*n
        pre1 = [0]*n
        ans = 0
        if s[0] == '0':
            pre0[0] = 1
        else:
            pre1[0] = 1
        for i in range(1,n):
            if s[i] == '0':
                pre0[i] = pre0[i-1] + 1
                pre1[i] = pre1[i-1]
            else:
                pre0[i] = pre0[i-1]
                pre1[i] = pre1[i-1] + 1
        # print(pre0)
        # print(pre1)
        for i in range(1,n-1):
            if s[i] == '0':
                # 010的情况
                # print(((pre1[i])*(pre1[-1]-pre1[i])))
                ans += (pre1[i]*(pre1[-1]-pre1[i]))
            else:
                # 101的情况
                # print(((pre0[i])*(pre0[-1]-pre0[i])))
                ans += (pre0[i]*(pre0[-1]-pre0[i]))
        return ans 