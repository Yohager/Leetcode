class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        tmp =  []
        n = len(word)
        i = 0
        while i < n:
            if word[i] in ['a','e','i','o','u']:
                s = word[i]
                j = i + 1
                while j < n:
                    if word[j] not in ['a','e','i','o','u']:
                        break 
                    else:
                        s += word[j]
                        j += 1
                if len(s) >= 5:
                    tmp.append(s)
                i = j + 1
            else:
                i += 1 
        #print(tmp)
        #tmp存储了所有的元音子串
        if not tmp:
            return 0
        for t in tmp:
            length = len(t)
            for l in range(5,length+1):
                for i in range(length-l+1):
                    #print(t[i:i+l])
                    cnt = 0
                    for r in ['a','e','i','o','u']:
                        if r in t[i:i+l]:
                            cnt += 1
                    if cnt == 5:
                        ans += 1
        return ans 
        