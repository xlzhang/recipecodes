class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        factor, count = 5, 0

        while True:
            curCount = n / factor
            if not curCount:
                break

            count += curCount
            factor *= 5

        return count
	
	def trailingZeroes(self,n):
		count = 0
		while n >= 5:
			count += n/5
			n /= 5
		return count
		
a = 101
b = Solution()
c = b.trailingZeroes(a)
print c
