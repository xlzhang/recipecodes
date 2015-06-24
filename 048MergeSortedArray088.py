class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        idx = m+n-1
        i = m-1
        j = n-1
        while i>=0 and j>=0:
            if nums1[i] >= nums2[j]:
                nums1[idx] = nums1[i]
                i -= 1
            else:
                nums1[idx] = nums2[j]
                j -= 1
            idx -= 1
        while j>=0:
            nums1[idx] = nums2[j]
            idx -= 1
            j -= 1
## The idea is to find the max value max(nums1,nums2) and place it into nums1 from the end
