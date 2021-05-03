class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        用counter不太好，还是得手动实现以下
        '''
        # c = collections.Counter(nums)
        # return c.most_common()[-1][0]
        n = len(nums)
        hashmap = collections.defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        for x in hashmap:
            if hashmap[x] == 1:
                return x