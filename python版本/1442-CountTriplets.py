class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        #a = b means a ^ b = 0
        for i in range(n-1):
            tmp = arr[i]
            for j in range(i+1,n):
                tmp ^= arr[j]
                if tmp == 0 and j > i:
                    ans += j-i
        return ans 