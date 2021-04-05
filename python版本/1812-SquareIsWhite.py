class Solution:
    def squareIsWhite(self, c: str) -> bool:
        if int(c[-1]) % 2 == 0:
            if c[0] == 'a' or c[0] == 'c' or c[0] == 'e' or c[0] == 'g':
                return True
            else:
                return False
        else:
            if c[0] == 'a' or c[0] == 'c' or c[0] == 'e' or c[0] == 'g':
                return False
            else:
                return True