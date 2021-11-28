class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = collections.Counter(list(word1))
        c2 = collections.Counter(list(word2))
        all_keys = list(set(c1.keys())) + list(set(c2.keys()))
        for key in all_keys:
            if key in c1 and key in c2:
                if abs(c1[key]-c2[key]) > 3:
                    return False 
            elif key in c1 and key not in c2:
                if c1[key] > 3:
                    return False 
            elif key not in c1 and key in c2:
                if c2[key] > 3:
                    return False 
        return True 