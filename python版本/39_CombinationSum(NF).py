class Solution:
    def combinationSum(self, candidates, target):
        result = []
        max_iterations = target//candidates[0] + 1
        iteration = 1
        while (iteration <= max_iterations):
            
