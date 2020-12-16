class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        def count_nums(tempstr):
            number0,number1=0,0
            for i in tempstr:
                if i == "0":
                    number0 += 1
                else:
                    number1 += 1
            return [number0,number1]
        #dp[i][j] = max{dp[i][j],1+dp[m-x,n-y]}
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        print(dp)
        for temp in strs:
            num0,num1 = count_nums(temp)
            j = m
            while j >= num0:
                k = n
                while k >= num1:
                    dp[j][k] = max(dp[j][k],1+dp[j-num0][k-num1])
                    k -= 1
                j -= 1
        return dp[m][n]

str1 = ["10","0001","111001","1","0"]
m = 4
n = 3
print(Solution.findMaxForm(Solution,str1,m,n))



