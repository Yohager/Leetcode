class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            if not arr:
                arr.append(nums[i])
            else:
                if nums[i] == arr[-1]:
                    continue 
                else:
                    arr.append(nums[i])
        ans = 0
        if len(arr) < 3:
            return 0
        n = len(arr)
        for i in range(1,n-1):
            if (arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1]):
                ans += 1
        return ans 