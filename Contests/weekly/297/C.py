import numpy as np 
class Solution:
    def distributeCookies(self, c: List[int], k: int) -> int:
        n = len(c)
        # tmp = np.array_split(c,k)
        # print(tmp)
        ans = float('inf')
        def sorted_k_partitions(seq, k):
            n = len(seq)
            groups = []  # a list of lists, currently empty

            def generate_partitions(i):
                if i >= n:
                    yield list(map(tuple, groups))
                else:
                    if n - i > k - len(groups):
                        for group in groups:
                            group.append(seq[i])
                            yield from generate_partitions(i + 1)
                            group.pop()

                    if len(groups) < k:
                        groups.append([seq[i]])
                        yield from generate_partitions(i + 1)
                        groups.pop()

            result = generate_partitions(0)

            # Sort the parts in each partition in shortlex order
            result = [sorted(ps, key = lambda p: (len(p), p)) for ps in result]
            # Sort partitions by the length of each part, then lexicographically.
            result = sorted(result, key = lambda ps: (*map(len, ps), ps))

            return result
        res = sorted_k_partitions(c,k)
        # print(res)
        for r in res:
            cur = 0 
            for x in r:
                cur = max(cur,sum(x))
            ans = min(ans,cur)
        return ans 


# 使用状态压缩dp
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # 答案与输入的顺序无关
        # 集合的划分问题
        # 存在消耗的概念 
        # 需要想到状态压缩dp
        # f[i][j]表示消耗了k个子序列，这些子序列组成了集合j
        # f[i][j] 枚举j的子集s
        # min max(f[i-1][j^s], sum[s]) for s in j 
        n = len(cookies)
        f = [[inf]*(1<<n) for _ in range(k)]
        s = [0] * (1<<n)
        for i in range(1<<n):
            for j in range(n):
                if (i >> j & 1):
                    s[i] += cookies[j]
        for i in range(1<<n):
            f[0][i] = s[i]
        for i in range(k):
            for j in range(1<<n):
                x = j 
                while x:
                    x = (x-1) & j 
                    f[i][j] = min(f[i][j],max(f[i-1][j^x],s[x]))
        return f[k-1][(1<<n)-1]

