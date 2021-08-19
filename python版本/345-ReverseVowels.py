class Solution:
    def reverseVowels(self, string1: str) -> str:
        if not string1:
            return ''
        n = len(string1)
        s = list(string1)
        l,r = 0,n-1
        d = ['a','o','e','i','u',"A","O","E","I","U"]
        while l <= r:
            if s[l] in d and s[r] in d:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in d and s[r] not in d:
                r -= 1
            elif s[l] not in d and s[r] in d:
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(s)