class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0][0] = 1
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                tmp = stones[i] - stones[j]
                #相邻石子之间的distance大于编号则必然不行
                if tmp > j + 1:
                    break 
                if tmp + 1 < n:
                    dp[i][tmp] = dp[j][tmp-1] | dp[j][tmp] | dp[j][tmp+1]
                else:
                    dp[i][tmp] = dp[j][tmp-1] | dp[j][tmp]  

                if i == n - 1 and dp[i][tmp] == 1:
                    return True
        return False