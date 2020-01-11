class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_char = {}
        left = 0
        right = 0
        result = 0
        max_len = 0
        while(right < len(s)):
            dict_char[s[right]] = dict_char.get(s[right],0) + 1
            max_len = max(max_len,dict_char[s[right]])
            while(right-left+1-max_len > k):
                dict_char[s[left]] -= 1
                left += 1
            result = max(result,right-left+1)
            right += 1
        return result


print(Solution.characterReplacement(Solution,"AABABBA",1))