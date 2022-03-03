### 一些模板

#### 二分查找

首先明确有时候有一些问题给定的是$O(\log N)$的时间复杂度的要求那么一定第一时间想到用二分查找的方法去做。

```python
def binary_search(l,r):
    while l < r:
        m = l + r // 2
        if f(m):
            return m 
        if g(m):
            r = m
        else:
            l = m + 1
    return l
```

其中的函数f(m)表示的是当中间位置的值满足搜索的要求时我们直接返回结果，如果结果满足的是g(m)，右指针左移到中间的位置，否则左指针右移到中间的位置。

给出一道题目：找到有序数组中某个值出现的区间范围，例如：[1,2,3,3,4,4,5]中3出现的索引范围是[2,3]，没有出现过的就是[-1,-1]. 要求$O(\log N)$的时间复杂度。

```python
class Solution:
    def searchRange(self, nums, target):
        lb = self.leftbound(nums,target)
        rb = self.rightbound(nums,target)
        if lb == rb:
            return [-1,-1]
        else:
            return [lb,rb-1]

    def leftbound(self,nums,target):
        l,r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m+1
            else:
                r = m 
        return l 

    def rightbound(self,nums,target):
        l,r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m+1
            else:
                r = m
        return l 
```

---

#### DP

路径dp

给定一个m*n的网格，只能向下或者向右移动，从左上到右下共计多少条路径。

dp[i][j]表示从0,0到i,j位置的总路径数量

**leetcode 63**

dp[i][j] = dp[i-1][j] + dp[i][j-1] (要么从左边，要么从上面)

讨论一些边界的情况：

```python
m,n = len(grid), len(grid[0])
dp = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
return dp[-1][-1]
```

为什么这个问题可以使用dp解决

**对于某一个状态来说，我们只需要关注状态对应的值，不需要关注状态如何转换过来的**

Note: 这里所说的不需要关注状态如何转换过来的表示的是不在意这个转换的过程，即：初始状态-下一个状态-...-最终的状态。

如果在grids中加上一些障碍物后

**leetcode 64**

```python
dp = [[1] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        dp[i][j] = 0 if grid[i][j] = 1 else 1 

for i in range(m):
    for j in range(n):
        if grid[i][j] != 1:
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]
return dp[-1][-1]
```

如果grids中存在权重，目标是找到路径中最小的权重和

**leetcode 65**

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = copy.deepcopy(grid)
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                elif i > 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
        return dp[-1][-1]
```

**leetcode 120**

当从rectangle变为triangle的情况下，最基础的做法比较简单：

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = copy.deepcopy(triangle)
        n = len(triangle)
        for i in range(1,n):
            for j in range(len(triangle[i])):
                # bug在于只能左右两边的位置
                # dp[i][j] = min(dp[i-1]) + triangle[i][j]
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = dp[i-1][-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])
```

直接沿用上一个问题的思路走，如果额外多一个$O(n)$的空间复杂度的限制，其中$n$表示为这个大的triangle的行数。


