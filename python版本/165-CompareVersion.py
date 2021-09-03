class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int,version1.split('.')))
        v2 = list(map(int,version2.split('.')))
        t = max(len(v1),len(v2))
        if t == len(v1):
            v2 = v2 + [0] * (t-len(v2))
        elif t == len(v2):
            v1 = v1 + [0] * (t-len(v1))
        i = 0
        while i < t:
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
            i += 1
        return 0