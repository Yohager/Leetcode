class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        n = len(wall)
        for i in wall:
            pos = 0
            for j in i[:-1]:
                pos += j
                d[pos] = d.get(pos,0) + 1
        if not d.values():
            return n
        else:
            return n - max(d.values())
