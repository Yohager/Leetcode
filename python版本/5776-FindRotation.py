class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def func(A):
            return list(map(list,zip(*A)))[::-1]
        if mat == target:
            return True
        for i in range(4):
            mat = func(mat)
            print(mat)
            if mat == target:
                return True
        return False