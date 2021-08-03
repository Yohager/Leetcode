class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        sumval = sum(milestones)
        maxval = max(milestones)
        if sumval < 2 * maxval:
            #此时表示不能够将最大的任务分批次完成，则返回的值为能够完成的最大的任务的那一部分
            return 2 * (sumval-maxval) + 1
        return sumval