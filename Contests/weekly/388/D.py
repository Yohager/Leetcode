'''
状态包含两个信息 前多少个数 划分为多少段
划分型dp 基础版本 O(n^2 * k)
1. 考虑从后往前思考
2. f[i][j]表示前j个数分为i段每一段选一个子数组的最大能量值
3. 不选num[j - 1], 则问题变为前j - 1个数分为i段 f[i][j - 1]
4. 选需要考虑选多少个的问题:
    f[i][j] = max(f[i - 1][L] + (s[j] - s[L]) * w) for L [i - 1, j - 1]
5. f[i][j] = max(f[i][j - 1], max(f[i - 1][L] + (s[j] - s[L]) * w) for L [i - 1, j - 1]) 
6. w = (-1)^(i + 1) * (k - i + 1)
7. 答案 f[k][n]
8. 初始值 f[0][j] = 0
         f[i][j < i] = -inf

优化 max(f[i - 1][L] + (s[j] - s[L]) * w) for L [i - 1, j - 1]
f[i][i] = 枚举 L = i - 1
f[i][i + 1] = 枚举 L = (i - 1, i)
f[i][i + 2] = 枚举 L = (i - 1, i, i + 1)

f[i][j - 1] = 枚举 L = (i - 1, i, ... , j - 2) => max已经计算出来
f[i][j] = 枚举 L = (i - 1, i, ... , j - 2, j - 1)

f[i][j] = max(f[i][j - 1], s[j] * w_i + maxv)

'''
class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        f = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            f[i][i - 1] = -inf
            maxv = -inf
            w = (1 if i % 2 else -1) * (k - i + 1)
            for j in range(i,  n - k + i + 1):
                maxv = max(maxv, f[i - 1][j - 1] - s[j - 1] * w) # 核心是这一步的优化
                f[i][j] = max(f[i][j - 1], s[j] * w + maxv)
        return f[k][n]

