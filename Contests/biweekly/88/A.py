class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        for w in word:
            cur = []
            for k, v in c.items():
                if k == w:
                    if v - 1 > 0:
                        cur.append(v - 1)
                else:
                    cur.append(v)
            if len(set(cur)) == 1:
                # print(cur)
                return True 
        return False 
            