class Solution:
    def findAnagrams(self, s: str, p: str):
        left = 0
        right = 0
        window = {}
        result = []
        match = 0
        needs = dict((i,p.count(i)) for i in p)
        while (right < len(s)):
            temp_1 = s[right]
            if temp_1 in needs.keys():
                window[temp_1] = window.get(temp_1,0) + 1
                if window[temp_1] == needs[temp_1]:
                    match += 1
            right += 1
            while (match == len(needs)):
                if right - left == len(p):
                    result.append(left)
                temp_2 = s[left]
                if temp_2 in needs.keys():
                    window[temp_2] -= 1
                    if window[temp_2] < needs[temp_2]:
                        match -= 1
                left += 1
        return result
    
s = "cbaebabacd"
p = "abc"
print(Solution.findAnagrams(Solution,s,p))





