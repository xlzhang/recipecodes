class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
		n = len(s)-1
		lastdigit = 0
		ret = 0
		dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
		while n>=0:
			if dict[s[n]]>= lastdigit:
				ret += dict[s[n]]
			else:
				ret -= dict[s[n]]
			lastdigit = dict[s[n]]
			n -= 1
		return ret
		
a = 'DCXXI'
b = Solution()
c = b.romanToInt(a)
print c
