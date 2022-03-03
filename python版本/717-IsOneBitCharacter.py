class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool: 
        n = len(bits)
        cnt = 0
        for i in range(n-2,-1,-1):
            if bits[i] == 1:
                cnt += 1
            else:
                break 
        return True if cnt % 2 == 0 else False 