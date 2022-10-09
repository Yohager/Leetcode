from sortedcontainers import SortedList 
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans = 0
        arr = [x-y for x,y in zip(nums1, nums2)]
        tmp = SortedList()
        for a in arr:
            ans += bisect.bisect_right(tmp, a + diff)
            tmp.add(a)
        return ans 