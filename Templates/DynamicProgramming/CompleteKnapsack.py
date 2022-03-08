'''
基本设定变化不大
c表示背包容量 v表示items的价值 w表示items的容量
完全背包问题考虑的是如果每种item可以无限取的情况下最大的价值
同样从0-1背包问题出发
dp[i][j]表示到i件item时剩余容量为j的情况下能够得到的最大的价值
与0-1背包最大的区别
每次遇到新的item时我们需要考虑是否要多次取当前的item
dp[i][j] = max(dp[i-1][j],dp[i-1][j-k*w[i]] + k*v[i])
即每一次我们要考虑当前最多能选多少个item i的问题
'''
def CompleteKnapsack(c,v,w):
    n = len(v)
    dp = [[0]*(c+1) for _ in range(n)]
    for i in range(c+1):
        if i > w[0]:
            k = i // w[0]
            dp[0][i] = k * v[0]
    
    for i in range(1,n):
        for j in range(c+1):
            no = dp[i-1][j]
            k = 0 
            yes = 0
            if j > w[i]:
                k = j // w[i]

            yes = dp[i-1][j-k*w[i]] + k*v[i]
            dp[i][j] = max(no,yes)
    return dp[-1][-1] 


'''
在0-1背包问题中状态转移方程: dp[j] = max(dp[j],dp[j-v[i]]+w[i])
考虑完全背包中的所有情况:
dp[i][j] = max(
    dp[i-1][j],
    dp[i-1][j-w[i]] + v[i],
    dp[i-1][j-2*w[i]] + 2*v[i],
    ...
    dp[i-1][j-k*w[i]] + k*v[i]
)
dp[i][j-w[i]] = max(
    dp[i-1][j-w[i]],
    dp[i-1][j-2*w[i]] + v[i],
    ...
    dp[i-1][j-k*w[i]] + (k-1)*v[i]
)
两者总是差了一个v[i]
完全背包的状态转移方程:
dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])
所以说对于
0-1背包问题 第i行的格子的值取决于i-1行正上方以及左边
完全背包问题 第i行的格子的值取决于i-1行正上方以及i行左边
'''
def CompleteKnapsack2(c,v,w):
    n = len(v)
    dp = [0] * (c+1)
    for i in range(n):
        for j in range(c+1):
            no = dp[j]
            yes = 0
            if j >= w[i]:
                yes = dp[j-w[i]] + v[i]
            dp[j] = max(no, yes)
    return dp[-1]




if __name__ == "__main__":
    c = 5
    v = [1,2]
    w = [1,2]
    print(CompleteKnapsack(c,v,w))
    print(CompleteKnapsack2(c,v,w))