class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        res = []
        for x in ghosts:
            res.append(abs(target[0]-x[0])+abs(target[1]-x[1]))
        dist = abs(target[0])+abs(target[1])
        if dist < min(res):
            return True 
        else:
            return False