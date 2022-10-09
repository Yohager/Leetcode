class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        '''
        考虑XOR的性质 贪心从前向后遍历置位数 
        1. 如果num1的置位数小于num2 考虑先将x表示为num1然后剩余的1从后向前添加
        2. 如果num1的置位数大于num2 贪心从前向后将num2加为1 没有了则全赋值为0
        '''
        v1 = bin(num1).count('1')
        v2 = bin(num2).count('1')
        if v1 == v2:
            return num1
        elif v1 < v2:
            x = num1 
            # 剩余 v2 - v1个
            # 从后向前添加
            left = v2 - v1
            cur = list(bin(x)[2:])
            if len(cur) < 32:
                cur = ['0'] * (32 - len(cur)) + cur 
            # n = len(cur)
            # print(cur)
            idx = len(cur) - 1
            while idx >= 0 and left > 0:
                if cur[idx] == '0':
                    cur[idx] = '1'
                    left -= 1
                idx -= 1
            return int(''.join(cur), 2)
        else:
            x = num1 
            left = v1 - v2
            cur = list(bin(x)[2:])
            if len(cur) < 32:
                cur = ['0'] * (32 - len(cur)) + cur 
            # 从后向前将'1'改为'0'
            idx = len(cur) - 1
            while idx >= 0 and left > 0:
                if cur[idx] == '1':
                    cur[idx] = '0'
                    left -= 1
                idx -= 1
            return int(''.join(cur), 2)