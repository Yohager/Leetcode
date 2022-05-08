class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cads = []
        for i in range(10):
            cur = str(i)*3
            if cur in num:
                cads.append(int(cur))
        if not cads:
            return ''
        maxv = max(cads)
        if maxv == 0:
            return '000'
        else:
            return str(maxv)
        