'''
给定一个set
返回set的所有子集
'''
import itertools


def Subsets1(arr):
    n = len(arr)
    ans = []
    for i in range(1 << n):
        cur = []
        for j in range(n):
            if (i >> j) & 1:
                cur.append(arr[j])
        ans.append(cur)
    return ans 

def Subsets2(nums):
    ans = []
    def dfs(arr,pos):
        nonlocal ans 
        ans.append(arr[:])
        for i in range(pos,len(nums)):
            arr.append(nums[i])
            dfs(arr,i+1)
            arr.pop()
    dfs([],0)
    return ans 
    

def Subsets3(arr):
    ans = []
    for i in range(len(arr)+1):
        ans += list(itertools.combinations(arr,i))
    return ans 


if __name__ == "__main__":
    print(Subsets1([1,2,3]))
    print(Subsets2([1,2,3]))
    print(Subsets3([1,2,3]))
