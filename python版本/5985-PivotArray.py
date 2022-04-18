class Solution:
    def pivotArray(self, nums: List[int], p: int) -> List[int]:
        l,r = [],[]
        e = []
        for num in nums:
            if num < p:
                l.append(num)
            elif num == p:
                e.append(num)
            else:
                r.append(num)
        return l + e + r