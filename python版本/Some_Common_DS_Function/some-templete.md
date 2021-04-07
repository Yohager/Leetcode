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

