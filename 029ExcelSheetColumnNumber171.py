class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
		n = len(s)
		if n ==1:
		    return ord(s[0])-64
		ret = 0
		i = 0
		for i in range(n):
			ret += (ord(s[i])-64)*26**(n-i-1)
		return ret
		
	def titleToNumber(self, s):
        return sum([j*26**i for i, j in enumerate(map(lambda x:ord(x)-64, s[::-1]))])
	
a = 'ABC'
b =Solution()
c = b.titleToNumber(a)
print c
