class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
		while 1:
			n = str(n)
			lenght = len(n)
			ret = 0
			for i in range(lenght):
				ret += int(n[i])**2
			if ret == 1:
				return True
			elif ret == 4:
				return False
			n = str(ret)
			
    def isHappy(self, n):
        stop = {1}
        while n not in stop:
            stop.add(n)
            n = sum(int(d)**2 for d in str(n))
        return n == 1
a = 2
b = Solution()
c = b.isHappy(a)
print c	
