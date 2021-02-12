class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 1
        l,r = 0,1
        ans = -1
        while r < n:
            if r < n - 1 and (arr[r]-arr[r-1])*(arr[r]-arr[r+1]) > 0:
                r += 1
            else:
                if arr[r] == arr[r-1]:
                    ans = max(ans, r-l)
                else:
                    ans = max(ans, r-l+1)
                l = r
                r += 1
        return ans
