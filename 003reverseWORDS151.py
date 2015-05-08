class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        ls = s.split()
        rs = [""]*len(ls)
        for i in range(len(ls)):
            rs[i] = ls[len(ls)-i-1]
        fs = " ".join(rs)
        return fs
