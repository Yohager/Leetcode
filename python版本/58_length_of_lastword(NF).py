class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == []:
            return 0
        list_str = s.split(' ')
        if '' in list_str:
            list_str.remove('')
        print(list_str)
        return len(list_str[-1])

            

if __name__ == '__main__':
    test = Solution
    result = test.lengthOfLastWord(test,"hello ab")
    print(result)