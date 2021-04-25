class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if len(set(word)) < 5:
            return 0
        d = {'a':1,'e':2,'i':3,'o':4,'u':5}
        s = []
        for i in word:
            s.append(d[i]) 
        #定义一个是否出现过的数组
        visit = [0,0,0,0,0]
        ans = 0
        t = 1
        for i in range(1, len(s)):
            if s[i] >= s[i-1]:
                t += 1
                visit[s[i-1]-1] = 1
                visit[s[i]-1] = 1
            else: 
                t = 1
                visit = [0,0,0,0,0]
            if sum(visit) == 5:
                ans = max(ans, t)
        return ans