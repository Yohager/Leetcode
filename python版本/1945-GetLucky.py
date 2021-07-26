class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ''
        for i in s:
            res += str(ord(i) - 96)
        print(res)
        for x in range(k):
            tmp = 0
            for j in res:
                tmp += int(j)
            res = str(tmp)
        return int(res)