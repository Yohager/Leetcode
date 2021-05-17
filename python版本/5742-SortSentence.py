class Solution:
    def sortSentence(self, s: str) -> str:
        tmp = s.split(' ')
        ans = []
        for i in tmp:
            a = list()
            for k in i:
                if k.isdigit():
                    a.append(k)
                    a.append(i)
                    break
            ans.append(a)
        ans.sort()
        res = []
        for x in ans:
            res.append(x[1][:-1])
        return ' '.join(res)