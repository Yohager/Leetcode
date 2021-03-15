class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        n = len(s)
        stack = []
        i = 0
        while i < n:
            if stack:
                if s[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)

