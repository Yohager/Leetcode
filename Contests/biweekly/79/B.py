class Solution:
    def largestWordCount(self, m: List[str], s: List[str]) -> str:
        c = Counter()
        n = len(m)
        for i in range(n):
            cur = m[i].split(' ')
            l = len(cur)
            c[s[i]] += l 
        cads = []
        cnt = c.most_common(1)[0][1]
        # print(cnt)
        for k in c.keys():
            if c[k] == cnt:
                cads.append(k)
        cads.sort(reverse=True)
        return cads[0]