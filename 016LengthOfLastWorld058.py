class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if s =="" or s ==" ":
            return 0
        flag = 0
        i = len(s)-1
        length = 0
        while i>=0:
            if s[i]==' ':
                i -= 1
            else:
                i -= 1
                length += 1
                if i < 0 or s[i] == ' ':
                    return length
        return 0
