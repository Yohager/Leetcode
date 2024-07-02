class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        arr = [x % 2 for x in nums]
        
        idx0 = 0
        idx1 = 0
        for i in range(n):
            if arr[i] == 0:
                idx0 = i
                break
        for i in range(n):
            if arr[i] == 1:
                idx1 = i
                break

        def calc(i, m, a):
            # 从i开始 取模为m的长度
            l = len(a)
            ans = 1
            cur = a[i]
            for j in range(i + 1, l):
                if (cur + a[j]) % 2 == m:
                    cur = a[j]
                    ans += 1
                else:
                    continue
            return ans 
        
        ans1 = calc(idx0, 0, arr)
        ans2 = calc(idx0, 1, arr)
        ans3 = calc(idx1, 0, arr)
        ans4 = calc(idx1, 1, arr)
        return max(ans1, ans2, ans3, ans4)
                

# solution 2 
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        def calc(n, m):
            left = [n, m]
            i = 1
            while left[i % 2] >= i:
                left[i % 2] -= i
                i += 1
            return i - 1
        
        return max(calc(red, blue), calc(blue, red))
