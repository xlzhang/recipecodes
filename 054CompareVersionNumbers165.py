from itertools import izip_longest
class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = (int(n) for n in version1.split('.'))
        v2 = (int(n) for n in version2.split('.'))
        for n1, n2 in izip_longest(v1, v2, fillvalue=0):
            if n1> n2:
                return 1
            elif n1< n2:
                return -1
        return 0

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
	def compareVersion(self, version1, version2):
		v1 = version1.split('.')
		v2 = version2.split('.')
		n1 = len(v1)
		n2 = len(v2)
		n = min(n1,n2)
		for i in range(n):
			if int(v1[i])> int(v2[i]):
				return 1
			elif int(v1[i])< int(v2[i]):
				return -1
		if n1 > n2 and int(v1[i+1]) !=0:
			return 1
		elif n1 < n2 and int(v2[i+1]) !=0:
			return -1
		return 0
	

	
a = '11.1'
b = '1.12'
c =Solution()
d = c.compareVersion(a,b)
print d
