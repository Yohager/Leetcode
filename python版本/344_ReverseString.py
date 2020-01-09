class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        i = 0
        j = length - 1
        while (i <= j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        return s


print(Solution.reverseString(Solution,["h","e","l","l","o"]))