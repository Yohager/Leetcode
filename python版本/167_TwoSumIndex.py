class Solution:
    def twoSum(self, numbers, target):
    	small = 0
    	big = len(numbers)-1
    	while (numbers[small] + numbers[big] != target):
    		if (numbers[small] + numbers[big] < target):
    			small += 1
    		else:
    			big -= 1
    	return [small+1,big+1]

if __name__ == '__main__':
	print(Solution.twoSum(Solution,[2,7,11,15],9))