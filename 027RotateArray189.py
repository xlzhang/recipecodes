class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
		def gcd(a,b):
			if b == 0:
				return a
			else:
				return gcd(b, a%b)
		
		n = len(nums)
		for i in range(gcd(n, k)):
			pre = nums[i]
			j = i
			while (j+k)%n != i:
				# temp = nums[(j+k)%n]
				# nums[(j+k)%n] = pre
				# pre = temp
				nums[(j+k)%n], pre = pre, nums[(j+k)%n]
				j = (j+k)%n
			nums[(j+k)%n] = pre
		return nums
		
    def rotate(self, nums, k):
		def reverse(nums, i, j):
			while i<= j:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
				j -= 1
			return nums
		k %= len(nums)
		reverse(nums, 0, len(nums)-1)
		reverse(nums, 0, k-1)
		reverse(nums, k, len(nums)-1)
		return nums
		
def main():
	a = [1,2,3,4]
	b = 5
	c = Solution()
	d = c.rotate(a,b)
	print d

if __name__ == "__main__":
	main()
