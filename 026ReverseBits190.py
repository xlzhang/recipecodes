class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        length = len(bin(n)[2:])
        zeros = ''.join(['0']*(32-length))
        binnum = zeros + bin(n)[2:]
        return int(binnum[::-1],2)
    
    def reverseBits(self, n):
        x = bin(n)[:1:-1].ljust(32,'0')
        return int(x,2)
