class Solution:
    def maxConsecutiveAnswers(self, ans: str, k: int) -> int:
        #考虑两种情况，一种是全部替换为T，一种是全部替换为F，分别计算最大数量
        def func(arr,s):
            n = len(arr)
            tmp = []
            for i in range(n):
                if arr[i] == s:
                    tmp.append(i)
            tmp.append(n)
            #此时tmp的长度为'T'或者'F'的个数+1
            #如果取不到k下标表示k的值大于所有的个数
            if k >= len(tmp):
                return n
            maxval = tmp[k]
            for j in range(k+1,len(tmp)):
                maxval = max(maxval,tmp[j]-tmp[j-k-1]-1)
            return maxval 
        
        return max(func(ans,'T'),func(ans,'F'))