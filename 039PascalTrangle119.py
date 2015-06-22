class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex < 2:
            return [1]*(rowIndex+1)
        ls = [1,1]
        for i in range(2,rowIndex+1):
            for j in range(i):
                if j == 0:
                    ret=[1]
                else:
                    ret.append(ls[j]+ls[j-1])
            ret.append(1)
            ls = ret
        return ret
