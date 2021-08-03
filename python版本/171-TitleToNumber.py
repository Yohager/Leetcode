class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        if n == 1:
            return ord(columnTitle[0]) - 64
        base = [1] * n 
        for i in range(1,n):
            base[i] = base[i-1] * 26 + 1
        #print(base)
        #计算差值
        diff = 0
        for x,y in enumerate(columnTitle):
            diff += 26 ** (n-1-x) * (ord(y)-ord("A"))
        #print(base[-1],diff)
        return base[-1] + diff



