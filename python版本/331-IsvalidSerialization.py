class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder: return False
        if preorder == "#": return True
        #print(len(preorder))
        preorder = preorder.split(",")
        #print(preorder)
        stack = []
        n = len(preorder)
        for i in range(n):
            stack.append(preorder[i])
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#" and stack[-3].isdigit():
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        #print(stack)
        return len(stack) == 1 and stack.pop() == "#"