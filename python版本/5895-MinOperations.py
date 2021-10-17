class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        from itertools import chain 
        arr = list(chain(*grid))
        arr.sort()
        n = len(arr)
        if len(set(arr)) == 1:
            return 0
        diff = []
        for i in range(1,len(arr)):
            diff.append(arr[i]-arr[i-1])
        for j in range(n-1):
            if diff[j] % x != 0:
                return -1 
        idx = n // 2 
        target = arr[idx]
        ans = 0
        for e in arr:
            ans += (abs(e-target) // x)
        return ans