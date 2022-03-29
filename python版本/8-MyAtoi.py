'''
如果使用正则表达式的话解法如下
class Solution:
    def myAtoi(self, s: str) -> int:
        MINV, MAXV = -2**31, 2**31-1
        ans = int(*re.findall('^[\+\-]?\d+',s.lstrip()))
        if ans < MINV:
            return MINV 
        elif ans > MAXV:
            return MAXV
        else:
            return ans 
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        MAXV = 2**31 - 1
        MINV = -2**31
        s = s.lstrip(' ')
        if not s:
            return 0
        n = len(s)
        idx = 0
        negative = False 
        if s[idx] == '-':
            idx += 1
            negative = True 
        elif s[idx] == '+':
            idx += 1 
        elif not s[idx].isdigit():
            return 0

        ans = 0
        while idx < n and s[idx].isdigit():
            cur = ord(s[idx]) - ord('0')
            # print(cur)
            if ans > (MAXV-cur) / 10:
                return MAXV if not negative else MINV 
            ans = ans*10 + cur 
            idx += 1
        return ans if not negative else -ans
