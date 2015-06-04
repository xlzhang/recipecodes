class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
		if a[0] == '0':
			return b
		if b[0] == '0':
			return a
		
		carry = 0
		absum = []
		i = len(a)-1
		j = len(b)-1
		if i < j:
			temp = a
			temp_i = i
			i = j
			a = b
			b = temp
			j = temp_i
		
		while j>=0:
			if int(a[i]) + int(b[j]) > 1:
				absum.append(str(carry))
				carry = 1
			else:
				temp = int(a[i]) + int(b[j]) + carry
				if temp>1:
					absum.append(str(0))
					carry=1
				else:
					absum.append(str(temp))
					carry = 0
			i -=1
			j -=1
		if carry == 0:
			while i >= 0:
				absum.append(str(int(a[i])))
				i -= 1
		else:
			while i >= 0:
				if int(a[i]) + carry >1:
					absum.append(str(0))
					carry = 1
				else:
				    absum.append(str(int(a[i]) + carry))
				    carry = 0
				i -= 1
		if carry == 1:
			absum.append(str(1))
		# k = len(absum)-2
		# ret = str(absum[len(absum)-1])
		# while k>=0:
			# ret += str(absum[k])
			# k -=1
		ret = ''.join(absum[::-1])
		return ret

	
	def addBinary(self, a, b):
        i, m, n, result, carry = 1, len(a), len(b), [], 0
        while i <= m or i <= n:
            temp = carry
            if i <= m:
                temp += int(a[-i])
            if i <= n:
                temp += int(b[-i])

            carry = temp / 2
            result.append(str(temp % 2))
            i += 1

        if carry:
            result.append(str(carry))

        return ''.join(result[::-1])
		
	def addBinary(self, a, b):
		return bin(int(a, 2)+int(b, 2))[2:]			

	def addBinary(self, a, b):
        return '{0:b}'.format(int(a, 2) + int(b, 2))
					
a = '101111'
b = '10'
c = Solution()
d = c.addBinary(a,b)
print d
