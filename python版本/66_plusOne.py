class Solution:
    def plusOne(self, digits):
        digits.reverse()
        number = 0
        for i in range(len(digits)):
            number += digits[i]*(10**i)
        number += 1
        return list(map(int,str(number)))

if __name__ == "__main__":
    test = Solution
    digits = [1,2,9]
    print(test.plusOne(test,digits))