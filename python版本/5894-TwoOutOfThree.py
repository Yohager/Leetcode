class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = set()
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        c3 = collections.Counter(nums3)
        for x1 in c1:
            if x1 in c2:
                ans.add(x1)
            if x1 in c3:
                ans.add(x1)
        for x2 in c2:
            if x2 in c1:
                ans.add(x2)
            if x2 in c3:
                ans.add(x2)
        for x3 in c3:
            if x3 in c1:
                ans.add(x3)
            if x3 in c2:
                ans.add(x3)
        return list(ans)