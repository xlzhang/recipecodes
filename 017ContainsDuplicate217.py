class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if nums == "":
            return True
        for i in range(len(nums)):
			if nums[i] in nums[:i]:
				return False
        return True
		
    def containsDuplicate(self, nums):
        i = 0
        arr = dict()
        for i in range(len(nums)):
            if nums[i] in arr:
                return True
            else:
                arr[nums[i]] = 1
        return False		

    def containsDuplicate(self, nums):
        new_set = set(nums)
        if len(new_set) == len(nums):
            return False
        else:
            return True
			
a = [1,2,3,4,5]
b = Solution()
c = b.containsDuplicate(a)
print c
