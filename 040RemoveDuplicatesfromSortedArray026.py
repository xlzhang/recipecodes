class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
		if not nums:
			return 0
		left = 0
		for right in range(1,len(nums)):
			if nums[right] != nums[left]:
				left += 1
				nums[left] = nums[right]
		return left+1
a = [1,1,2,2,2,3,4]
b = Solution()
c = b.removeDuplicates(a)
print c
