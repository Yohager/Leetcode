import sortedcontainers
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        record = []
        for l,r,h in buildings:
            record.append((l,-h))
            record.append((r,h))
        record.sort()
        print(record)
        cur = sortedcontainers.SortedList([0])
        prev = 0
        for x,y in record:
            if y < 0:
                cur.add(y)
            else:
                cur.remove(-y)
            
            cur_max = -cur[0]
            if cur_max != prev:
                ans.append([x,cur_max])
            prev = cur_max
        return ans