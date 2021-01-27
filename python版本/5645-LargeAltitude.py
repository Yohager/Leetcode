class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        heights = list()
        heights.append(0)
        n = len(gain)
        for i in range(n):
            heights.append(heights[i]+gain[i])
        #print(heights)
        return max(heights)