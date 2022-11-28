class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = -1 
        acc = list(accumulate(list(range(1,n+1))))
        # print(acc)
        for i in range(1, n+1):
            tmp = acc[-1] - acc[i-2] if i >= 2 else acc[-1]
            if acc[i-1] == tmp:
                ans = i
                
        return ans 