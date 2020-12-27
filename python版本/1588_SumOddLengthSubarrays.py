class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        length = len(arr)
        times = length if length % 2 == 1 else length - 1
        temp = list(range(1,times+1,2))
        ans = 0
        #print(temp)
        for i in temp:
            temp1 = 0
            for j in range(length):
                if j + i > length:
                    break
                temp1 += sum(arr[j:j+i])
            ans += temp1
        return ans
