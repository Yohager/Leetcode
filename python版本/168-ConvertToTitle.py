class Solution:
    def convertToTitle(self, c: int) -> str:
        res = ''
        while c:
            c -= 1
            res += chr(c%26+65)
            c //= 26 
        return res[::-1]

