class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        ans1 = list()
        ans2 = list()
        n = len(s)
        for i in range(n):
            if s[i] not in dict1.keys():
                dict1[s[i]] = str(i)
                ans1.append(str(i))
            else:
                ans1.append(dict1[s[i]])
        
        for j in range(n):
            if t[j] not in dict2.keys():
                dict2[t[j]] = str(j)
                ans2.append(str(j))
            else:
                ans2.append(dict2[t[j]])
        
        for k in range(n):
            if ans1[k] != ans2[k]:
                return False
        return True