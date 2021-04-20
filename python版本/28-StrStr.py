class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(haystack)
        if haystack == needle:
            return 0
        l,r = 0,0
        while l <= n-len(needle):
            if haystack[l] == needle[0]:
                k = 1
                r = l+1
                while k < len(needle):
                    if haystack[r] != needle[k]:
                        break
                    r += 1
                    k += 1
                if k == len(needle):
                    return l
            l += 1

        return -1