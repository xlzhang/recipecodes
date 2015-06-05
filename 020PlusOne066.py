class Solution:
	# @param {integer[]} digits
	# @return {integer[]}
	def plusOne(self, digits):
		ret = []
		i = len(digits)-1
		carry = 0
		while i>=0:
			if i == len(digits)-1:
				mod = (digits[i] + 1 + carry)%10
				carry = (digits[i] + 1 + carry)/10
				ret.append(mod)
			elif carry == 1:
				mod = (digits[i] + carry)%10
				carry = (digits[i] + carry)/10
				ret.append(mod)
			else:
				temp = ret[::-1]
				ret = digits[:i+1]+temp
				return ret
			i -= 1
		ret.append(carry)
		return ret[::-1]
	
	def plusOne(self, digits):
		ret = []
		i = len(digits)-1
		carry = 1
		while i>=0:
			mod = (digits[i] + carry)%10
			ret.append(mod)
			carry = (digits[i] + carry)/10
			i -= 1
			if carry == 0:
				return digits[:i+1] + ret[::-1]
		ret.append(1)
		return ret[::-1]
	
	def plusOne(self, digits):
		carry = 1
		i = len(digits)-1
		while i >= 0:
			temp = digits[i]
			digits[i] = (digits[i] + carry)%10
			carry = (temp + carry)/10
			i -= 1
			if carry == 0:
				return digits
		digits.insert(0,carry)
		return digits
		
	def plusOne(self, digits):
        return map(int,list(str(int(''.join(map(str,digits)))+1)))

a = [9,9,9]
b =Solution()
c = b.plusOne(a)
print c
