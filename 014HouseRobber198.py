class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        bag = []
        bag.append(nums[0])
        bag.append(max(nums[0], nums[1]))
        for i in range(2,len(nums)):
            max_money = max(bag[i-1], bag[i-2] + nums[i])
            bag.append(max_money)
        return bag[len(nums)-1]
