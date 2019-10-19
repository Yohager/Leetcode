class Solution:
    def strStr(self,haystack,needle) -> int:
        if (needle == ''):
            return 0
        if (len(haystack) < len(needle)):
            return -1
        length = len(haystack)
        i = 0
        while (i < length):
            if (haystack[i] == needle[0]):
                temp = haystack[i:i+len(needle)]
                if (temp == needle):
                    return i
                else:
                    i += 1
                    continue
                '''
                j = i
                k = 0
                #count = 0
                while (k < len(needle) and j < length):
                    if (haystack[j] == needle[k]):
                        j += 1
                        k += 1
                    else:
                        break
                #print(i)
                if (k == len(needle)):
                    return i
                else:
                    i += 1
                    continue
                '''
            i += 1
        return -1

