class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        alpha = ['a','e','i','o','u','A','E','I','O','U']
        n = len(s)
        a = s[:int(n/2)]
        b = s[int(n/2):]
        ans1 = 0
        ans2 = 0
        for i in a:
            if i in alpha:
                ans1 += 1
        for j in b:
            if j in alpha:
                ans2 += 1
        return ans1 ==  ans2
                