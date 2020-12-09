class Subsets:
	def __init__(self, nums):
		self.subsets = [[]]
		self.nums = nums

	def Subsetfind(self): 
	    for i in range(len(self.nums)): 
	        orig = self.subsets[:] 
	        new = self.nums[i] 
	        for j in range(len(self.subsets)): 
	            self.subsets[j] = self.subsets[j] + [new] 
	        self.subsets = orig + self.subsets 

print("Enter list of distinct numbers")
nums = list(map(int, input().split()))
subset = Subsets(nums)
subset.Subsetfind()
print("Subsets are : ", subset.subsets)
