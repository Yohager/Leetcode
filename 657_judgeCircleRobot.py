class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

            





if __name__ == "__main__":
    test = Solution
    print(test.judgeCircle(test,'LL'))