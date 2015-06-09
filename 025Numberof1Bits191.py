class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ret = 0
        if n == 0:
            return ret
        while n!=0:
            ret += n%2
            n = n/2
        return ret
