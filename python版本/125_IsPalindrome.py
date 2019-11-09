class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
        s = ''.join(filter(str.isalnum,s)).lower()
        i = 0
        j = len(s) - 1
        while (i < j):
            if (s[i] == s[j]):
                i += 1
                j -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    test = Solution
    s = "A man, a plan, a canal: Panama"
    print(test.isPalindrome(test,s))