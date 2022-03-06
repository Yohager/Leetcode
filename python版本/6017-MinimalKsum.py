class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        '''
        极端情况：nums刚好是一个有序的数组，追加的k就是直接用数组求和
        '''
        ans = 0
        nums.sort()
        if nums[0] != 1:
            nums = [1] + nums
            ans = 1
            k -= 1
        n = len(nums)
        diff = [0]
        #print(nums)
        for i in range(1,n):
            # if nums[i] == nums[i-1]:
            #     continue 
            diff.append(nums[i]-nums[i-1]-1)
        #print(diff)
        idx = 0 
        while idx < n and k > 0:
            #print('k is here',k)
            if diff[idx] == 0 or diff[idx] == -1:
                idx += 1
                continue
            if k >= diff[idx]: 
                k -= diff[idx]
                # 求和加上一些值
                #print('here',nums[idx-1],diff[idx])
                ans += ((nums[idx-1]+1+nums[idx]-1)*diff[idx]) // 2
                #print('here',k,ans)
            else:
                #此时k已经不够用了
                #print('aaahere',idx,k,ans)
                ans += ((nums[idx-1]+1+nums[idx-1]+k)*k) // 2
                k = 0
                #print('new here',k,ans)
                
            idx += 1
        if k > 0:
            #直接在最大值后面追加
            #print(k)
            extra = ((nums[-1]+1+nums[-1]+k)*k) // 2
            ans += extra
        return ans
        