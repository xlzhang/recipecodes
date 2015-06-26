class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
		ret = []
		n = len(nums)
		if n==1:
			ret.append(str(nums[0]))
			return ret
		start = 0
		steps = 0
		for i in range(1,n):
			if nums[i]-1 != nums[i-1]:
				if steps>=1:
					ls = str(nums[start]) + "->" + str(nums[start + j])
				else:
					ls = str(nums[start])
				ret.append(ls)
				start = i
				steps = 0
				if i == n-1:
					ls = str(nums[start])
					ret.append(ls)
			elif i != n-1:
				steps += 1
			else:
				ls = str(nums[start]) + "->" + str(nums[i])
				ret.append(ls)
		return ret
		
a = [0,5,9]
b = Solution()
c = b.summaryRanges(a)
print c
