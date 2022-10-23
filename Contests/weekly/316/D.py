class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        o1, e1 = [], []
        o2, e2 = [], []
        for x, y in zip(nums, target):
            if x % 2:
                o1.append(x)
            else:
                e1.append(x)
            if y % 2:
                o2.append(y)
            else:
                e2.append(y)
        # print(o1,o2,e1,e2)
        o1.sort()
        e1.sort()
        o2.sort()
        e2.sort()
        s1 = sum([abs(x-y) for x, y in zip(o1,o2)])
        s2 = sum([abs(x-y) for x, y in zip(e1,e2)])
        return (s1 + s2) // 4
        
            