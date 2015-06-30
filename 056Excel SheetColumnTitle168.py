class Solution:
    # @param {integer} n
    # @return {string}
	def convertToTitle(self, n):
		ret = ''
		while n>0:
			last = n%26
			if not last:
				ret += 'Z'
				n = n/26 - 1
			else:
				ret += chr(ord('A') + last - 1)
				n = n/26
		return ret[::-1]
	
	def convertToTitle(self, n):
		ds = {i+1: chr(ord('A')+i) for i in range(26)}
		ret = ''
		while n > 0:
			last = n%26 or 26
			ret += ds[last]
			n = (n-1)/26
		return ret[::-1]
			
a = 2*26 + 3
b = Solution()
c = b.convertToTitle(a)
print c
