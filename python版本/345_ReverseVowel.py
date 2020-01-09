class Solution:
    def reverseVowels(self, s) -> str:
        s = list(s)
        length = len(s)
        i = 0
        j = length - 1
        vowel = ['a','e','i','o','u','A','E','U','I','O']
        while (i <= j):
            if (s[i] in vowel and s[j] in vowel):
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            elif (s[i] in vowel and s[j] not in vowel):
                j -= 1
            elif (s[i] not in vowel and s[j] in vowel):
                i += 1
            else:
                i += 1
                j -= 1
        
        return ''.join(s)


print(Solution.reverseVowels(Solution,"hello"))