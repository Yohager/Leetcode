class Solution:
    def totalSteps(self, nums):
        st = []
        for num in nums:
            max_t = 0 
            while st and st[-1][0] <= num:
                max_t = max(max_t, st.pop()[1])
            if st:
                max_t += 1
            ans = max(ans, max_t)
            st.append((num, max_t))
        return ans 