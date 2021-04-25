class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = collections.Counter(sentence)
        if len(d) == 26:
            return True
        else:
            return False