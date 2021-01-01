class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        k = 0
        stack = []
        while popped:
            while stack and stack[-1] == popped[i]:
                stack.pop(-1)
                popped.pop(i)
            if stack and k >= len(pushed) and popped[i] != stack[-1]:
                return False
            while k < len(pushed):
                if popped[i] == pushed[k]:
                    popped.pop(i)
                    k += 1
                    break
                else:
                    stack.append(pushed[k])
                    k += 1
        return True