class Solution:
    def check(self, nums: List[int]) -> bool:
        nums1 = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(nums1[(i+j)%n])
            res.append(tmp)
        print(res)
        return True if nums in res else False