class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+1)
        for f,l,num in bookings:
            diff[f-1] += num 
            diff[l] -= num 
        # print(diff)
        ans = [0] * n
        cur = diff[0]
        for i in range(1,n+1):
            ans[i-1] = cur 
            cur += diff[i]
        return ans 
