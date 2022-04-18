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