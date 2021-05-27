class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ans = 0
        def func(arr,target):
            ans = 0
            for i in range(len(arr)):
                cnt = 0
                if arr[i] == target:
                    for j in range(i,len(arr)):
                        if arr[j] != arr[i]:
                            break 
                        cnt += 1
                    ans = max(ans,cnt)
            return ans             
        a = func(s,'0')
        b = func(s,'1')
        #print(a,b)
        return b > a
                    
                