from sets import Set
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        nums_set=Set(nums)
        for i in nums:
            if target - i in nums_set:
                index1 = nums.index(i)
                index2 = nums.index(target-i)
                
                if index1 < index2:
                    return [index1+1, index2+1]
                elif index1 == index2:
                    nums[index1] += 1
                    try:
                        index2=nums.index(i)
                    except ValueError:
                        nums[index1]-=1
                        continue
                    else:
                        return [index1+1,index2+1]
                else:
                    return [index2+1, index1+1]
