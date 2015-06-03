class Solution:
    # @param {string} s
    # @return {string}
    
	def ispalindrome(self, s):
		left = 0
		right = len(s)-1
		while left<=right:
			if s[left] == s[right]:
				left += 1
				right -= 1
			else:
				return 0
		return 1
		
	def longestPalindrome(self, s):
		if len(s) < 2:
			return s
		sub_max = 0
		left = 0
		right = len(s)-1
		i = 0
		j = len(s)-1
		while left < len(s):
			left = i
			while s[left] != s[right] and left<right:
				right -= 1
			if self.ispalindrome(s[left:right+1]):
				if sub_max < len(s[left:right+1]):
					sub_max = len(s[left:right+1])
					sub_str = s[left:right+1]
				left += 1
				i += 1
				right = len(s)-1
			elif left == right:
				left += 1
				i += 1
				right = len(s)-1
			else:
				right -= 1
		return sub_str

		
	def longestPalindrome(self,s):
		if len(s)<2:
			return s
		start = 0
		max_len = 1
		table = [[0 for x in range(1000)] for x in range(1000)]
		for i in range(len(s)):
			table[i][i] = 1
			start = i
			max_len = 1
		for i in range(len(s)-1):
			if s[i] == s[i+1]:
				table[i][i+1] = 1
				start = i
				max_len = 2
		
		for k in range(3,len(s)+1):
			for i in range(len(s)-k+1):
				j = i + k -1
				if s[i] == s[j] and table[i+1][j-1]:
					table[i][j] = 1
					start = i
					max_len = k
		return s[start: start+max_len]
		

	def longestPalindrome(self,s):
		length = len(s)
		if length<2:
			return s
		new_s = '%'
		for i in range(length):
			new_s += '#' + s[i]
		new_s += '#&'
		
		new_len = len(new_s)
		center = 0l
		right = 0
		new_p = [0]*new_len
		for i in range(1,new_len-1):
			i_mirror = center - (i-center)
			if right > i:
				new_p[i] = min(right-i, new_p[i_mirror])
			else:
				new_p[i] = 0
			while new_s[i+new_p[i]+1] == new_s[i-new_p[i]-1]:
				new_p[i] += 1
			if i+new_p[i] > right:
				center = i
				right = i+new_p[i]
		max_len = max(new_p)
		center = new_p.index(max_len)
		start = (center - max_len - 1)/2
		end = (center - max_len - 1)/2 + max_len
		# sub_str = s[(center - max_len - 1)/2:(center - max_len - 1)/2 + max_len + 1]
		sub_str = s[start:end]
		return sub_str
