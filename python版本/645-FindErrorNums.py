class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # ans = []
        # n = len(nums)
        # if nums[0] == nums[1]:
        #     return [1,2]
        # for i in range(1,n):
        #     if nums[i-1] == nums[i]:
        #         ans.append(nums[i-1])
        #         ans.append(nums[i-1]+1)
        #         break
        # return ans 
        c = collections.Counter(nums)
        tmp = c.most_common(1)[0][0]
        #print(tmp)
        n = len(nums)
        seq = [i for i in range(1,n+1)]
        sum1 = sum(seq)
        sum2 = sum(list(set(nums)))
        return [tmp,sum1-sum2]
