class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ret = defaultdict(list)
        n = len(arr)
        for i in range(n):
            # 遍历arr[i]的所有子字符串
            length = len(arr[i])
            for l in range(length):
                for r in range(l, length):
                    substr = arr[i][l : r + 1]
                    tag = True
                    for j in range(n):
                        if i != j:
                            if substr in arr[j]:
                                tag = False
                                break 
                    if tag:
                        ret[i].append(substr)
        res = []
        for i in range(n):
            if not ret[i]:
                res.append("")
            else:
                res.append(sorted(ret[i], key=lambda x : (len(x), x))[0])
        return res
