class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        tmp = []
        for i in dominoes:
            i.sort()
            tmp.append(''.join(list(map(str,i))))
        from collections import Counter
        res = Counter(tmp)
        ans = 0
        for i in res:
            num = res[i]
            ans += sum(list(range(1,num)))
        return ans
        