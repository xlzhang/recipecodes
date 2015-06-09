class Solution:
	# @param {integer[]} nums
    # @return {integer}
	def majorityElement(self, nums):
		count = 0
		i = 0
		j = nums[0]
		for i in range(len(nums)):
			if count ==0:
				j = nums[i]
			if nums[i] == j:
				count += 1
			else:
				count -= 1
		return j
		
	def majorityElement(self, nums):
		return sorted(nums)[len(nums) / 2]
		
	def majorityElement(self, nums):
		count = {}
		for i in range(len(nums)):
			if nums[i] in count:
				count[nums[i]] += 1
			else:
				count[nums[i]] = 1
			if count[nums[i]] > len(nums)/2:
				return nums[i]
a = [1,2,2,3,2,5,2]
b = Solution()
c = b.majorityElement(a)
print c
