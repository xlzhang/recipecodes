class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
		if n == 1:
			return "1"
		if n ==2:
			return "11"
		oldstr = str(11)
		for i in range(n-2):
			newstr = ""
			count = 1
			for j in range(len(oldstr)-1):
				if oldstr[j] == oldstr[j+1]:
					count += 1
					if j == len(oldstr)-2:
						newstr = newstr + str(count) + oldstr[j]
				else:
					newstr = newstr + str(count) + oldstr[j]
					count = 1
			if oldstr[j+1] != oldstr[j]:
				newstr = newstr + str(1) + oldstr[j+1]
			oldstr = newstr
		return newstr

	def countAndSay(self, n):
		if n == 1:
			return "1"
		if n ==2:
			return "11"
		oldstr = str(11)
		for i in range(n-2):
			newstr = ""
			count = 1
			for j in range(1,len(oldstr)):
				if oldstr[j] == oldstr[j-1]:
					count += 1
					if j == len(oldstr)-1:
						newstr = newstr + str(count) + oldstr[j]
				else:
					newstr = newstr + str(count) + oldstr[j-1]
					count = 1
					if j == len(oldstr)-1:
						newstr = newstr + str(count) + oldstr[j]

			oldstr = newstr
		return newstr
a = 4
b = Solution()
c = b.countAndSay(a)
print c
