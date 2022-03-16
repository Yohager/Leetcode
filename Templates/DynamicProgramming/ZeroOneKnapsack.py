'''
基本的0-1背包问题
dp的定义 dp[i][j]表示为当到第i个物品的情况下剩余容量为j时最大的价值
基本的转移过程为：
对于第i件物品: 我们有选或者不选两种决策
不选的话直接转移到dp[i-1][j]即上一个物品时还有j容量的最大价值
如果选的话: 首先要保证当前的容量大于等于w[i]，然后得到的价值为
dp[i][j-w[i]] + v[i]
两种情况取较高者: dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
'''
def knapsack(c,v,w):
    # c表示总量，v表示每个item的价值，w表示每个item的重量
    n = len(v)
    dp = [[0]*(c+1) for _ in range(n)]
    #特殊处理第一个item
    for i in range(c+1):
        dp[0][i] = v[0] if i >= w[0] else 0 
    
    # 考虑剩余的情况
    for i in range(1,n):
        for j in range(c+1):
            if j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
    print(dp)
    return dp[-1][-1]


'''
进一步我们可以发现空间是可以优化的
因为对于到第i个物品来说, 状态转移只取决于两个值: i-1行的j位置和i-1行的j-w[i]位置
所以实际上只依赖于从j开始左边的位置
'''
def knapsack2(c,v,w):
    n = len(v)
    dp1 = [0] * (c+1)
    for i in range(n):
        for j in range(c,w[i]-1,-1):
            v1 = dp1[j]
            v2 = dp1[j-w[i]] + v[i]
            dp1[j] = max(v1,v2)
    print(dp1)
    return dp1[-1]



if __name__ == "__main__":
    cap = 4
    vals = [4,2,3]
    weights = [4,2,3]
    print(knapsack(cap,vals,weights))
    print(knapsack2(cap,vals,weights))
