class Solution:
    def maxBottlesDrunk(self, nb: int, ne: int) -> int:
        if nb == 0:
            return 0
        record = 0
        while nb > 0:
            record += nb
            eb = nb
            nb = 0
            while eb >= ne:
                eb -= ne
                ne += 1
                record += 1
                eb += 1
            # print(nb, eb, ne, record)
        # print(nb, eb, ne, record)
        return record
            
