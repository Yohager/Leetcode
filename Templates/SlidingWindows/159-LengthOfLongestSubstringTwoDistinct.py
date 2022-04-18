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