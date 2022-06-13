from decimal import Decimal
class Solution:
    def discountPrices(self, s: str, d: int) -> str:
        s = s.split(' ')
        for i,v in enumerate(s):
            if v[0] == '$' and len(v) > 1:
                if v[1:].isdigit():
                    tmp = '%.2f'
                    x = (1.00-d*0.01) * float(v[1:])
                    x = tmp % x
                    s[i] = '$' + str(x)
        return ' '.join(s)