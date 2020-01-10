class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        left = 0
        right = 0
        needs = dict((i,t.count(i)) for i in t)
        window = {}
        minlen = len(s)
        match = 0
        while (right < len(s)):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] = window.get(c1,0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1
            while (match == len(needs)):
                if right - left < minlen:
                    start = left
                    minlen = right - left
                c2 = s[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return '' if minlen == len(s) else s[start:start+minlen]


S = "ADOBECODEBANC"
T = "ABC"

print(Solution.minWindow(Solution,S,T))