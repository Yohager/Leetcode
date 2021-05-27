class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(sorted(words))
        tmp =  c.most_common(k)
        ans = []
        for i in tmp:
            ans.append(i[0])
        return ans 