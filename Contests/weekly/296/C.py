class Solution:
    def arrayChange(self, nums: List[int], op: List[List[int]]) -> List[int]:
        d = {}
        for i,e in enumerate(nums):
            d[e] = i
        
        for x,y in op:
            d[y] = d[x]
            d.pop(x)
        res = [0] * len(nums)
        for k,v in d.items():
            res[v] = k 
        return res 

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {}
        for x,y in reversed(operations):
            mp[x] = mp.get(y,y)
        # print(mp)
        return [mp.get(v,v) for v in nums]