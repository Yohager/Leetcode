class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr = title.split()
        return ' '.join([s.capitalize() if len(s) > 2 else s.lower() for s in arr])