class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return str(0)
        d = "0123456789abcdef"
        ans = ''
        while num and len(ans) < 8:
            ans = d[num & 0xf] + ans 
            num >>= 4 
        return ans