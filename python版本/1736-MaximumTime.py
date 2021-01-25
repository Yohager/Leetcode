class Solution:
    def maximumTime(self, t: str) -> str:
        ans = []
        if t[0] == '?' and t[1] == '?':
            ans.append('2')
            ans.append('3')
        elif t[0] != '?' and t[1] != '?':
            ans.append(t[0])
            ans.append(t[1])
        elif t[0] == '?' and t[1] != '?':
            if int(t[1]) <= 3:
                ans.append('2')
            else:
                ans.append('1')
            ans.append(t[1])
        elif t[0] != '?' and t[1] == '?':
            if t[0] == '2':
                ans.append(t[0])
                ans.append('3')
            else:
                ans.append(t[0])
                ans.append('9')           
        ans.append(':')
        if t[3] == '?' and t[4] == '?':
            ans.append('5')
            ans.append('9')
        elif t[3] != '?' and t[4] != '?':
            ans.append(t[3])
            ans.append(t[4])
        elif t[3] == '?' and t[4] != '?':
            ans.append('5')
            ans.append(t[4])
        elif t[3] != '?' and t[4] == '?':
            ans.append(t[3])
            ans.append('9')
        return ''.join(ans)