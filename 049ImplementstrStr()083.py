class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
		if not haystack and not needle:
			return 0
		elif not haystack:
			return -1
		elif not needle:
			return 0
		i = 0
		j = 0
		m = len(haystack)
		n = len(needle)
		if m<n:
			return -1
		while i<m:
			if i+n <= m and haystack[i:i+n] == needle:
				return i
			i += 1
		return -1
					
a = "mississippi"
b = "issipi"
c = Solution()
d = c.strStr(a,b)
print d
