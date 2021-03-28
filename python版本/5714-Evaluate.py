class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dict1 = {}
        for i in knowledge:
            dict1[i[0]] = i[1]
        ans = ''
        i = 0
        flag = 0
        tmp = ''
        while i < len(s):
            if s[i] == '(':
                flag = 1
                i += 1
            while flag == 1:
                if s[i] == ')':
                    if tmp in dict1:
                        ans += dict1[tmp]
                    else:
                        ans += '?'
                    flag = 0
                    tmp = ''
                    i += 1
                    break
                tmp += s[i]
                i += 1
            if i == len(s): return ans
            if s[i]!= '(' and s[i] != ')':
                ans += s[i]
                i += 1
        #print(ans)
        
        return ans