class Solution:
    def maximumUnits(self, b, n: int) -> int:
        #先根据第二个参数sort一下
        b.sort(reverse=True,key=lambda x:x[1])
        ans = 0
        for i in range(len(b)):
            print(n)
            if b[i][0] <= n:
                n -= b[i][0]
                ans += b[i][0]*b[i][1]
            else:
                n -= n
                ans += n * b[i][1]
            #print(ans)
            if n == 0:
                break
        return ans
                    

b = [[1,3],[2,2],[3,1]]
n = 4

print(Solution.maximumUnits(Solution,b,n))