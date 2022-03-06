class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = {}
        ans = []
        for i,x in enumerate(mapping):
            d[i] = x 
        for i,num in enumerate(nums):
            s = list(map(int,list(str(num))))
            res = ''
            for x in s:
                res += str(d[x])
            ans.append([int(res),i])
        ans.sort(key=lambda x:[x[0],x[1]])
        res = []
        for a in ans:
            res.append(nums[a[1]])
        return res 
                
            