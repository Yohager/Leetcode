class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word == word[0].upper() + word[1:].lower():
            return True 
        else:
            return False 