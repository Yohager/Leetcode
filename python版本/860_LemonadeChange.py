class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = [0,0]
        i = 0
        while i < len(bills):
            #如果收到的是5直接接收
            if bills[i] == 5:
                counts[0] += 1
            #如果收到的是10先判断5是否还有，有则接收，没有则返回false
            elif bills[i] == 10:
                if counts[0] > 0:
                    counts[0] -= 1
                    counts[1] += 1
                else:
                    return False
            #如果收到的是20，优先判断是否有一个10和一个5，如果没有则判断是否有3个5，都没有则返回false
            elif bills [i] == 20:
                if counts[0]>0 and counts[1]>0:
                    counts[0] -= 1
                    counts[1] -= 1
                elif counts[0] >= 3:
                    counts[0] -= 3
                else:
                    return False
            i += 1
        return True
                