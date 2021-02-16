class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        count = r * c
        l = len(nums)
        w = len(nums[0])
        tmp = l * w
        if count != tmp:
            return nums
        arr = []
        for i in range(l):
            for j in range(w):
                arr.append(nums[i][j])
        res = []
        for i in range(r):
            res.append(arr[i*c:i*c+c])
        return res