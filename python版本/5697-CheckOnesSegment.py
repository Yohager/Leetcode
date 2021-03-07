class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if not s: return False
        n = len(s)
        tmp = 0
        for i in range(n-1,-1,-1):
            if s[i] == '1':
                tmp = i
                break
        #检查0-tmp之间是否全为1，如果有不为1的就返回错误
        if tmp == 0:
            return True
        for j in range(tmp):
            if s[j] != '1':
                return False
        return True
                