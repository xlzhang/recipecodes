class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
		if len(s) < 2:
			return True
		ret = {}
		i = 0
		while i < len(s):
			if not ret.has_key(s[i]):
				if t[i] not in ret.values():
					ret[s[i]] = t[i]
				else:
					return False
			elif ret[s[i]] != t[i]:
				return False
			i += 1
		return True
		
a = 'paper'
b = 'title'
c = Solution()
d = c.isIsomorphic(a,b)
print d
