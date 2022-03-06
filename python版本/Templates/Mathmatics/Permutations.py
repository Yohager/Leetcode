from itertools import permutations
from turtle import left

'''
here we give three ways to generate permutations for an array or an string 
'''

class Permutations:
    def __init__(self,nums) -> None:
        self.nums = nums 
        self.length = len(self.nums)
    
    def Method1(self):
        return permutations(self.nums,self.length)
    
    def Method2(self,arr):
        # using dfs
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return [arr]
        
        res = []
        for i in range(len(arr)):
            cur = arr[i]
            left_s = arr[:i] + arr[i+1:]
            for x in self.Method2(left_s):
                res.append([cur]+x)
        return res

    def Method3(self):
        res = []
        nums = self.nums 
        if not nums:
            return res 
        def dfs(arr,tmp):
            if not arr:
                res.append(tmp)
                return 
            for i in range(len(arr)):
                dfs(arr[:i]+arr[i+1:],tmp + [arr[i]])
        dfs(nums,[])
        return res 

if __name__ == "__main__":
    test = Permutations(['a','b','c'])
    print(list(test.Method1()))
    print(test.Method2(['a','b','c']))
    print(test.Method3())
