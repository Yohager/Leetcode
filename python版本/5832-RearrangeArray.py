class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # n = len(nums)
        # tmp = []
        # if n % 2 == 0:
        #     l = nums[:n//2]
        #     r = nums[n//2:]
        #     for i,j in zip(l,r):
        #         tmp.append(i)
        #         tmp.append(j)
        # else:
        #     l = nums[:n//2]
        #     r = nums[n//2+1:]
        #     for i,j in zip(l,r):
        #         tmp.append(i)
        #         tmp.append(j)
        #     tmp.append(nums[n//2])
        # return tmp
        n = len(nums)
        if n == 3:
            if nums[0] + nums[2] == 2*nums[1]:
                nums[0],nums[1] = nums[1],nums[0]
                return nums
        nums.sort()
        l = nums[:n//2]
        r = nums[n//2:]
        l.sort()
        r.sort(reverse=True)
        ans = []
        print(l,r)
        if n % 2 == 0:
            for i,j in zip(l,r):
                ans.append(i)
                ans.append(j)
        else:
            for i,j in zip(l,r[:-1]):
                ans.append(i)
                ans.append(j)
            ans.append(r[-1])
        return ans 