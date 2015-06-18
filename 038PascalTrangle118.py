class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
		pt = [[1] for i in range(numRows)]
		if numRows == 1:
			return [1]
		if numRows == 2:
			return [[1],[1,1]]
		pt = [[1] for i in range(numRows)]
		pt[1].append(1)
		for i in range(2,numRows):
			for j in range(1,i):
				newadd = pt[i-1][j] + pt[i-1][j-1]
				pt[i].append(newadd)
			pt[i].append(1)
		return pt
a = 6
b = Solution()
c = b.generate(a)
print c
