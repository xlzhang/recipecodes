class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
		if strs == "" or len(strs) == 0:
		    return ""
		for i in range(len(strs[0])):
			for j in range(len(strs)):
				if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
					return strs[0][:i]
		return strs[0]
