class Solution:
    def calculateTax(self, b: List[List[int]], ic: int) -> float:
        if ic == 0:
            return 0
        if ic <= b[0][0]:
            return 0.01 * ic * b[0][1]
        ans = 0
        n = len(b)
        cur = ic
        idx = -1
        d = [b[0][0]] * n 
        for j in range(1,n):
            d[j] = b[j][0] - b[j-1][0]
        # print(d)
        for i in range(n):
            if ic < b[i][0]:
                idx = i 
                break 
            ans += d[i] * b[i][1] * 0.01 
        if idx > 0 and idx < n:
            ans += (ic -  b[idx-1][0]) * b[idx][1] * 0.01
        return ans 
        
            
            
            