class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        # from sortedcontainers import SortedSet
        l,r = 0,0
        diff = 0
        arr = []
        while r < n:
            if r - l > k:
                arr.remove(nums[l])
                l += 1
            idx = bisect.bisect_left(arr,nums[r]-t)
            if arr and idx >= 0 and idx < len(arr) and abs(arr[idx] - nums[r])<= t:
                return True
            bisect.insort(arr,nums[r])
            r += 1
        return False
