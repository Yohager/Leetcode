class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = Counter()
        for i in range(len(nums)):
            if nums[i] == key:
                if i < len(nums)-1:
                    d[nums[i+1]] += 1
        #print(d)
        return d.most_common(1)[0][0]