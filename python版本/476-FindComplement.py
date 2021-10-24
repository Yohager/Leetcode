class Solution:
    def findComplement(self, num: int) -> int:
        temp = str(bin(num))[2:]
        res = ''
        for x in temp:
            if x == '0':
                res += '1'
            else:
                res += '0'
        return int(res,2)