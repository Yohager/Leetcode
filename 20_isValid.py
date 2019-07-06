class Solution:
    def isValid(self, s: str) -> bool:
        list_s = list(s)
        stack = []
        mapping = [('(',')'),('[',']'),('{','}')]
        if list_s == []:
            return True
        if len(list_s)%2 != 0:
            return False
        for i in range(len(list_s)):
            stack.append(list_s[i])
            if len(stack) >= 2 and (stack[-2],stack[-1]) in mapping:
                stack.pop()
                stack.pop()
        #print(stack)
        return stack == []


        '''
        for i in range(len(list_s)-1):
            if (list_s[i],list_s[i+1]) in mapping:
                list_s.remove(list_s[i])
                list_s.remove(list_s[i+1])
        return len(list_s)
        '''


test = Solution
result = test.isValid(test,'([])')
print(result)