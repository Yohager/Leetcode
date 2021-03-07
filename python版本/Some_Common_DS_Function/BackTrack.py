res = []
path = []
def backtrack(notexplore, res, path):
    if 未探索区域满足结束条件:
        res.add(path)
        return 
    
    for choice in 未探索区域当前可能的选择:
        if 当前的选择满足条件:
            path.add(当前选择)
            backtrack(新的未探索区域, res, path)
            path.pop()