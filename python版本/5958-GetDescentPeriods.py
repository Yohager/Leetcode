class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        arr = []
        ans = 0
        n = len(prices)
        i = 0 
        while i < n:
            tmp = 1
            j = i + 1 
            while i < n and j < n and prices[j] == prices[i]-1:
                tmp += 1
                i += 1
                j += 1
            arr.append(tmp)
            i += 1
        for a in arr:
            ans += ((1+a)*a//2)
        return ans 