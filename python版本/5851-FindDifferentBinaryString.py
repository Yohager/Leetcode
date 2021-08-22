class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # maxval = 2**n
        # ans = []
        # for x in nums:
        #     ans.append(int(x,2))
        # #ans.sort()
        # for i in range(0,n+1):
        #     if i not in ans:
        #         tmp = bin(i)[2:]
        #         if len(tmp) == n:
        #             return tmp
        #         else:
        #             diff = n - len(tmp)
        #             return '0'*diff + tmp
        d = set(nums)
        import itertools
        ans = []
        for i in itertools.product('01', repeat = n):
            ans.append(''.join(i))
        for x in ans:
            if x not in d:
                return x