"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        q = []
        ans = 0
        for i in employees:
            if i.id == id:
                for k in i.subordinates:
                    q.append(k)
                ans += i.importance
        while q:
            tmp = q[0]
            for j in employees:
                if j.id == tmp:
                    for x in j.subordinates:
                        q.append(x)
                    ans += j.importance
            q.pop(0)
        return ans
