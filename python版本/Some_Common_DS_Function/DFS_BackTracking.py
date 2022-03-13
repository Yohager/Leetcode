#回溯算法和DFS求解全排列问题的模板

回溯的基本思路
def backtrack(参数):
	if (终止条件):
		添加结果
		return 
	for (选择 当前层集合中的元素):
		处理当前的节点
		backtrack(路径, 选择列表)
		回溯撤销


class BackTracking:
    def dfs_backtracking(self,nums):
        def dfs(nums,size,depth,path,used,ans):
            if depth == size:
                ans.append(list(path))
                return
            
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums,size,depth+1,path,used,ans)
                    used[i] = False
                    path.pop()
        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        ans = []
        dfs(nums,size,0,[],used,ans)
        return ans

if __name__ == "__main__":
    nums = [1,2,3]
    print(BackTracking.dfs_backtracking(BackTracking,nums))

    
