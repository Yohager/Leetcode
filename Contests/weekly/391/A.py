class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumv = sum(list(map(int, list(str(x)))))
        return sumv if x % sumv == 0 else -1
