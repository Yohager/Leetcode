class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        ans = []
        o,e = 0,0
        for i in range(n):
            if i % 2 == 0:
                ans.append(even[e])
                e += 1
            else:
                ans.append(odd[o])
                o += 1
        return ans class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        ans = []
        o,e = 0,0
        for i in range(n):
            if i % 2 == 0:
                ans.append(even[e])
                e += 1
            else:
                ans.append(odd[o])
                o += 1
        return ans 