class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        arr = [1]
        f1,f2 = 1,1
        while f2 <= k:
            arr.append(f2)
            tmp = f2 
            f2 = f1 + f2 
            f1 = tmp 
        # print(arr)
        ans = 0
        for i in range(len(arr)-1,-1,-1):
            if arr[i] <= k:
                ans += 1
                k -= arr[i]
            if k == 0:
                break
        return ans 