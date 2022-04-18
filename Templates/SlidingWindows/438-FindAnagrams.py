class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pc = {}
        for x in p:
            pc[x] = pc.get(x,0) + 1
        l,r = 0,0
        n = len(s)
        sc = {}
        ans = []
        while l < n and r < n:
            while r - l < len(p):
                sc[s[r]] = sc.get(s[r],0) + 1
                r += 1
            if r - l == len(p):
                # print(sc,pc)
                if sc == pc:
                    ans.append(l)
                cur = s[l]
                sc[cur] -= 1
                if sc[cur] == 0:
                    sc.pop(cur)
                l += 1
        return ans 