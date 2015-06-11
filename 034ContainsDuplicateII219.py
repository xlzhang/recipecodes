class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        numdict = {}
        n = 0
        while n<len(nums):
            if nums[n] not in numdict:
                numdict[nums[n]] = n
            else:
                if n-numdict[nums[n]]<=k:
                    return True
                else:
                    numdict[nums[n]] = n
            n += 1
        return False
            
			
	def containsNearbyDuplicate(self, nums, k):
		numdict = dict()
		for pos, value in enumerate(nums):
			numdict.setdefault(value,[]).append(pos)
		for key in numdict:
			if len(numdict[key]) > 1:
				for i in range(len(numdict[key]) -1):
					if numdict[key][i+1] - numdict[key][i]<=k:
						return True
		return False
		
a = [1,0,1,1]
b = 1
c = Solution()
d = c.containsNearbyDuplicate(a,b)
print d
