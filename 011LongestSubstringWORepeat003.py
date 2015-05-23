class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        i = 1
        j = 0
        k = 0
        length = len(s)
        max_len = 1
        temp_len = 1
        while i < length:
            while s[i] != s[k]:
                temp_len += 1
                if temp_len > max_len:
                    max_len = temp_len
                k += 1
                if k == i:
                    break
            if k == i:
                k = j
            else:
                k = k + 1
                j = k
            temp_len = 1
            i += 1
        return max_len
