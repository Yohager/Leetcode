### 滑动窗口
---

#### 基本套路

- step.1 定义需要维护的变量: 如最小长度，最大长度，哈希表等等
- step.2 定义窗口的左右端点进行窗口的滑动
- step.3 更新需要维护的变量
- step.4 存在两种情况: 窗口大小固定/窗口大小可变
- step.5 返回答案

注意step.4中的两种情况

- 窗口大小固定 使用if判断当前长度是否达到限定长度,如果达到了则左指针向前移动，保证下一次右指针向右移动时窗口大小保持不变, 左指针移动之前先更新需要维护的变量。
- 窗口大小可变 涉及到窗口大小是否可变的问题, 如果不合法往往使用一个while循环不断移动左指针从而剔除非法元素直到窗口再次合法, 同样的在移动左指针之前不断更新需要维护的变量。

#### 经典题目

**Leetcode 643 子数组最大平均数I**
```
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = -float('inf') # 定义需要维护的值
        l,r = 0,0
        n = len(nums)
        total = 0 # 定义需要维护的值
        while l < n and r < n:
            while r-l < k: # 当前窗口还没有达到需要的大小
                total += nums[r]
                r += 1
            if r-l == k: # 当前窗口达到了要求的大小
                ans = max(ans,total/k)
                total -= nums[l] # 移动左指针前更新需要维护的变量的大小
                l += 1
        return ans 
```

**Leetcode 3 无重复字符的最长子串**
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 # 定义需要维护的值
        l,r = 0,0
        n = len(s)
        d = {} # 定义需要维护的值
        while l < n and r < n:
            d[s[r]] = d.get(s[r],0) + 1 
            if len(d) == r - l + 1: # keys的数量等于区间的长度则表示当前无重复的元素
                ans = max(ans,len(d))

            while len(d) < r - l + 1: # 如果当前keys的数量小于区间长度则有重复元素
                # 有重复元素
                cur = s[l]
                d[cur] -= 1 # 调整hash map
                if d[cur] == 0:
                    d.pop(cur)
                l += 1
            r += 1
        return ans 
```

**Leetcode 159 至多包含两个不同字符的最长子串**
```
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0 # 定义需要维护的值
        l,r = 0,0
        n = len(s)
        d = {} # 定义需要维护的值
        while l < n and r < n:
            d[s[r]] = d.get(s[r],0) + 1 
            if len(d) <= 2: # 如果当前hash map的元素个数小于等于2更新结果
                ans = max(ans,r-l+1)

            while len(d) > 2: # 如果当前hash map的元素个数大于2
                cur = s[l]
                d[cur] -= 1 # 调整hash map
                if d[cur] == 0:
                    d.pop(cur)
                l += 1
            r += 1
        return ans 
```

**Leetcode 209 长度最小的子数组**
```
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        ans = float('inf') # 定义需要维护的值
        total = 0 # 定义需要维护的值
        while l < n and r < n:
            total += nums[r]
            if total >= target:
                ans = min(ans,r-l+1)
            
            while total >= target:
                ans = min(ans,r-l+1)
                total -= nums[l]
                l += 1
            r += 1
        return ans if ans != float('inf') else 0
```

**Leetcode 1695 删除子数组的最大得分** 

```
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0 # 维护变量
        l,r = 0,0
        n = len(nums)
        total = 0 # 维护变量
        s = {} # 维护变量
        while l < n and r < n:
            total += nums[r]
            s[nums[r]] = s.get(nums[r],0) + 1
            if len(s) == r - l + 1:
                ans = max(total,ans)
            
            while len(s) < r - l + 1:
                total -= nums[l]
                s[nums[l]] -= 1
                if s[nums[l]] == 0:
                    s.pop(nums[l])
                l += 1
            r += 1
        return ans 
```

**Leetcode 438 找到字符串中所有字母异位词**

```
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pc = {}
        for x in p:
            pc[x] = pc.get(x,0) + 1
        l,r = 0,0
        n = len(s)
        sc = {}
        ans = []
        while l < n and r < n:
            while r - l < len(p):
                sc[s[r]] = sc.get(s[r],0) + 1
                r += 1
            if r - l == len(p):
                # print(sc,pc)
                if sc == pc:
                    ans.append(l)
                cur = s[l]
                sc[cur] -= 1
                if sc[cur] == 0:
                    sc.pop(cur)
                l += 1
        return ans 
```

**Leetcode 567 字符串的排列**
(这个问题和438题几乎一模一样)

```
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1), len(s2)
        if n1 > n2:
            return False 
        
        l,r = 0,0 
        d1 = {}
        d2 = {}
        for x in s1:
            d1[x] = d1.get(x,0) + 1
        
        while l < n2 and r < n2:
            while r - l < n1:
                d2[s2[r]] = d2.get(s2[r],0) + 1
                r += 1
            
            if r - l == n1:
                if d1 == d2:
                    return True 
                cur = s2[l]
                d2[cur] -= 1 
                if d2[cur] == 0:
                    d2.pop(cur)
                l += 1
        return False
```

**Leetcode 487 最大连续1的个数II**

```

```

**Leetcode 1004 最大连续1的个数III**

**Leetcode 1208 尽可能使字符串相等**

**Leetcode 1052 爱生气的书店老板**

**Leetcode 1423 可获得的最大点数**

**Leetcode 1151 最少交换次数来组合所有的1**

