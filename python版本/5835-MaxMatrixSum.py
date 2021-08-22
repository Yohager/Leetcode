class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0 
        flag = False
        minval = 1000000
        tmp = []
        for m in matrix:
            for x in m:
                ans += abs(x)
                if x < 0:
                    tmp.append(x)
                if x == 0:
                    flag = True
                minval = min(minval,abs(x))
        if len(tmp) % 2 == 0 or flag:
            return ans 
        else:
            return ans - 2*minval