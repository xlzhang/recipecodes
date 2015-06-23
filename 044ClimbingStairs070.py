class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n<3:
            return n
        a1 = 1
        a2 = 2
        for i in range(3,n+1):
            temp = a2
            a2 = a1+a2
            a1 = temp
        return a2
